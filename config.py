"""
Configuration module for AI_Toolbox
Reads model configuration and generates all derived paths and names
"""
import json
import os
from pathlib import Path

# Get the base directory
BASE_DIR = Path(__file__).parent

def load_config():
    """Load configuration from config.json"""
    config_path = BASE_DIR / "config.json"
    with open(config_path, 'r') as f:
        return json.load(f)

def get_model_config():
    """Get all model-related paths and names"""
    config = load_config()
    model_id = config['model_id']
    
    # Extract model name from HuggingFace ID (e.g., "google/gemma-3-1b-it" -> "gemma-3-1b-it")
    model_name = model_id.split('/')[-1]
    
    # Generate all paths and names
    return {
        'model_id': model_id,
        'model_name': model_name,
        'dataset_name': config.get('dataset_name', 'databricks/databricks-dolly-15k'),
        
        # Local directories
        'base_model_dir': f"./Outputs/{model_name}",
        'fine_tuned_dir': f"./Outputs/fine-tuned-{model_name}-yaseen",
        'merged_model_dir': "./Outputs/merged-model",
        'results_dir': "./Outputs/results",
        
        # GGUF output
        'gguf_filename': f"{model_name}-yaseen.gguf",
        'gguf_path': f"Outputs\\{model_name}-yaseen.gguf",
        
        # Ollama model name
        'ollama_model_name': f"{model_name}-yaseen",
        
        # Tokenizer model path
        'tokenizer_model_src': f"Outputs\\{model_name}\\tokenizer.model",
        'tokenizer_model_dst': "Outputs\\merged-model\\tokenizer.model"
    }

def save_config(model_id, dataset_name=None):
    """Update the configuration file"""
    config = {
        'model_id': model_id
    }
    if dataset_name:
        config['dataset_name'] = dataset_name
    else:
        # Keep existing dataset_name if not provided
        try:
            existing = load_config()
            config['dataset_name'] = existing.get('dataset_name', 'databricks/databricks-dolly-15k')
        except:
            config['dataset_name'] = 'databricks/databricks-dolly-15k'
    
    config_path = BASE_DIR / "config.json"
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"Configuration updated:")
    print(f"  Model ID: {model_id}")
    print(f"  Dataset: {config['dataset_name']}")

if __name__ == "__main__":
    # Test the configuration
    cfg = get_model_config()
    print("Current Configuration:")
    print(json.dumps(cfg, indent=2))
