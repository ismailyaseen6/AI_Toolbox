from transformers import AutoModelForCausalLM, AutoTokenizer
import sys
import os

# Add parent directory to path to import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from config import get_model_config

cfg = get_model_config()
model_name = cfg['model_id']
print(f"Using model: {model_name}")

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto"
)

prompt = "Give me a short introduction to LLMs"
messages = [
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

model_inputs = tokenizer(text, return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=32768
)

output_ids = generated_ids[0][len(model_inputs.input_ids[0]):].tolist()

try:
    index = len(output_ids) - output_ids[::-1].index(151668)
except ValueError:
    index = 0

thinking_content = tokenizer.decode(output_ids[:index], skip_special_tokens=True)
content = tokenizer.decode(output_ids[index:], skip_special_tokens=True)

print("Thinking:", thinking_content)
print("Content:", content)