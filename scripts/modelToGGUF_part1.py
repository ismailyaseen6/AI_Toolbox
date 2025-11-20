from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    "./Outputs/gemma-3-1b-it",
    dtype=torch.float16,
    device_map="auto"
)

# Load and merge LoRA weights
model = PeftModel.from_pretrained(base_model, "./Outputs/fine-tuned-gemma-3-1b-it-yaseen")
merged_model = model.merge_and_unload()

# Save merged model
merged_model.save_pretrained("./Outputs/merged-model")
tokenizer = AutoTokenizer.from_pretrained("./Outputs/gemma-3-1b-it")
tokenizer.save_pretrained("./Outputs/merged-model")