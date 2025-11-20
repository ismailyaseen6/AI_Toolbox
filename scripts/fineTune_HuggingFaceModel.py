import torch
from transformers import (
    AutoTokenizer,
    AutoModelForCausalLM,
    TrainingArguments,
    Trainer,
    BitsAndBytesConfig,
)
from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
from datasets import load_dataset
from huggingface_hub import snapshot_download
import sys
import os

# Add parent directory to path to import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from config import get_model_config

cfg = get_model_config()
print(f"Using model: {cfg['model_id']}")
print(f"Base model directory: {cfg['base_model_dir']}")
print(f"Fine-tuned output: {cfg['fine_tuned_dir']}")

# Download if not exists
if not os.path.exists(cfg['base_model_dir']):
    print("Downloading model...")
    snapshot_download(repo_id=cfg['model_id'], local_dir=cfg['base_model_dir'], local_dir_use_symlinks=False, revision="main")

# Configuration
MODEL_NAME = cfg['base_model_dir']
DATASET_NAME = cfg['dataset_name']
OUTPUT_DIR = cfg['fine_tuned_dir']
MAX_LENGTH = 512


def load_model_and_tokenizer(model_name):
    """Load and configure the model and tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    tokenizer.pad_token = tokenizer.eos_token

    quantization_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )
    
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        dtype=torch.float16,
        device_map="auto",
        quantization_config=quantization_config,
        use_cache=False  # Disable cache for gradient checkpointing compatibility
    )
    
    return model, tokenizer


def setup_lora(model):
    """Configure and apply LoRA to the model."""
    model = prepare_model_for_kbit_training(model)
    
    lora_config = LoraConfig(
        r=16,
        lora_alpha=32,
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj"],
        lora_dropout=0.05,
        bias="none",
        task_type="CAUSAL_LM",
    )
    
    return get_peft_model(model, lora_config)


def prepare_dataset(tokenizer, dataset_name):
    """Load and tokenize the dataset."""
    try:
        # Try loading with train split first
        dataset = load_dataset(dataset_name, split="train")
    except Exception as e:
        print(f"Could not load 'train' split: {e}")
        try:
            # Try loading test split if train doesn't exist
            dataset = load_dataset(dataset_name, split="test")
            print("Using 'test' split instead")
        except Exception as e2:
            print(f"Could not load 'test' split: {e2}")
            # Load entire dataset without specifying split
            dataset = load_dataset(dataset_name)
            # Get the first available split
            if isinstance(dataset, dict):
                split_name = list(dataset.keys())[0]
                dataset = dataset[split_name]
                print(f"Using '{split_name}' split")
            else:
                print("Using default dataset structure")
    
    # Limit dataset size for faster training (take first 1000 samples)
    if len(dataset) > 1000:
        dataset = dataset.select(range(1000))
        print(f"Limited dataset to 1000 samples for faster training")
    
    def tokenize_function(examples):
        # Try to detect the dataset structure and adapt
        try:
            texts = [
                f"Instruction: {instr}\n{f'Context: {ctx}\n' if ctx else ''}Response: {resp}"
                for instr, ctx, resp in zip(
                    examples["instruction"], examples["context"], examples["response"]
                )
            ]
        except KeyError:
            # If the expected columns don't exist, try alternative formats
            if "text" in examples:
                texts = examples["text"]
            elif "prompt" in examples and "completion" in examples:
                texts = [f"{p}\n{c}" for p, c in zip(examples["prompt"], examples["completion"])]
            elif "question" in examples and "answer" in examples:
                texts = [f"Question: {q}\nAnswer: {a}" for q, a in zip(examples["question"], examples["answer"])]
            else:
                # Fallback: use the first text-like column
                text_columns = [col for col in examples.keys() if isinstance(examples[col][0], str)]
                if text_columns:
                    texts = examples[text_columns[0]]
                    print(f"Using column '{text_columns[0]}' as text source")
                else:
                    raise ValueError(f"Could not find suitable text columns in dataset. Available columns: {list(examples.keys())}")
        
        result = tokenizer(texts, truncation=True, padding="max_length", max_length=MAX_LENGTH)
        result["labels"] = result["input_ids"]
        return result
    
    return dataset.map(tokenize_function, batched=True, remove_columns=dataset.column_names)


def main():
    # Load model and tokenizer
    model, tokenizer = load_model_and_tokenizer(MODEL_NAME)
    
    # Setup LoRA
    model = setup_lora(model)
    
    # Prepare dataset
    tokenized_dataset = prepare_dataset(tokenizer, DATASET_NAME)
    
    # Training configuration
    training_args = TrainingArguments(
        output_dir=cfg['results_dir'],
        per_device_train_batch_size=8,  # Increased for RTX 4070
        gradient_accumulation_steps=1,
        optim="paged_adamw_8bit",  # Use 8bit optimizer for better memory efficiency
        learning_rate=2e-4,
        max_steps=100,
        warmup_steps=10,
        save_steps=10,
        logging_steps=10,
        fp16=True,
        group_by_length=True,
        gradient_checkpointing=True,  # Enable for memory efficiency
    )
    
    # Data collator (not needed since we're padding in tokenization)
    data_collator = None
    
    # Train
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        data_collator=data_collator,
    )
    trainer.train()
    
    # Save fine-tuned model
    model.save_pretrained(OUTPUT_DIR)
    tokenizer.save_pretrained(OUTPUT_DIR)
    print(f"Model saved to {OUTPUT_DIR}")


if __name__ == "__main__":
    main()