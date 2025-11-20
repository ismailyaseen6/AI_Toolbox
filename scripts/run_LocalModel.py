from transformers import AutoModelForCausalLM, AutoTokenizer
from huggingface_hub import snapshot_download

model_id = "google/gemma-3-1b-it"
snapshot_download(repo_id= model_id, local_dir="./Outputs/gemma-3-1b-it", local_dir_use_symlinks=False, revision="main")

model_name = "./Outputs/gemma-3-1b-it"

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