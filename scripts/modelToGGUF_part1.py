from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import sys
import os

# Add parent directory to path to import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from config import get_model_config

cfg = get_model_config()
print(f"Loading base model from: {cfg['base_model_dir']}")
print(f"Loading fine-tuned weights from: {cfg['fine_tuned_dir']}")
print(f"Saving merged model to: {cfg['merged_model_dir']}")

# Load base model
base_model = AutoModelForCausalLM.from_pretrained(
    cfg['base_model_dir'],
    dtype=torch.float16,
    device_map="auto"
)

# Load and merge LoRA weights
model = PeftModel.from_pretrained(base_model, cfg['fine_tuned_dir'])
merged_model = model.merge_and_unload()

# Save merged model
merged_model.save_pretrained(cfg['merged_model_dir'])
tokenizer = AutoTokenizer.from_pretrained(cfg['base_model_dir'])
tokenizer.save_pretrained(cfg['merged_model_dir'])