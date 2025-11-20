# Configuration Guide

## Overview

AI_Toolbox now uses a centralized configuration system that allows you to easily switch between different HuggingFace models. All scripts and batch files automatically read from the configuration.

## Quick Start

### 1. Configure Your Model

**Interactive Mode:**
```bash
python configure.py
```

**Direct Mode:**
```bash
python configure.py set google/gemma-3-1b-it
```

**View Current Configuration:**
```bash
python configure.py show
```

### 2. Run the Pipeline

After configuration, run the pipeline as normal:
```bash
python launcher.py
```
Or:
```bash
setup.bat
Run.bat
```

## How It Works

### Configuration File: `config.json`

The `config.json` file stores your model preferences:

```json
{
  "model_id": "google/gemma-3-1b-it",
  "dataset_name": "databricks/databricks-dolly-15k"
}
```

### Automatic Path Generation

The system automatically generates all necessary paths and names from your model ID:

- **Model ID**: `google/gemma-3-1b-it`
- **Model Name**: `gemma-3-1b-it` (extracted)
- **Base Model Dir**: `./Outputs/gemma-3-1b-it`
- **Fine-tuned Dir**: `./Outputs/fine-tuned-gemma-3-1b-it-yaseen`
- **GGUF Filename**: `gemma-3-1b-it-yaseen.gguf`
- **Ollama Model Name**: `gemma-3-1b-it-yaseen`

## Switching Models

To switch to a different model, simply reconfigure and run:

```bash
# Switch to Llama 2
python configure.py set meta-llama/Llama-2-7b-hf

# Switch to Mistral
python configure.py set mistralai/Mistral-7B-v0.1

# Switch to Phi-2
python configure.py set microsoft/phi-2
```

All scripts will automatically use the new model configuration.

## Example Model IDs

Here are some popular HuggingFace model IDs you can use:

- `google/gemma-3-1b-it`
- `google/gemma-2-2b-it`
- `meta-llama/Llama-2-7b-hf`
- `meta-llama/Llama-2-7b-chat-hf`
- `mistralai/Mistral-7B-v0.1`
- `mistralai/Mistral-7B-Instruct-v0.2`
- `microsoft/phi-2`
- `TinyLlama/TinyLlama-1.1B-Chat-v1.0`

## Custom Dataset

You can also specify a custom dataset:

```bash
python configure.py set google/gemma-3-1b-it your-dataset/dataset-name
```

## Configuration Module

For advanced users, you can import the configuration in your own scripts:

```python
from config import get_model_config

cfg = get_model_config()
print(f"Using model: {cfg['model_id']}")
print(f"Output path: {cfg['base_model_dir']}")
```

## Files Modified by Configuration System

The following files automatically read from `config.json`:

### Python Scripts:
- `scripts/download_HuggingFaceBaseModel.py`
- `scripts/fineTune_HuggingFaceModel.py`
- `scripts/modelToGGUF_part1.py`
- `scripts/run_LocalModel.py`
- `scripts/run_Transformers_Huggingface.py`

### Batch Files:
- `scripts/modelToGGUF_part2.bat`
- `scripts/ollamaImportGGUF.bat`

## Troubleshooting

**Issue**: "Module 'config' not found"
**Solution**: Make sure you're running scripts from the project root directory.

**Issue**: Configuration not updating
**Solution**: Run `python configure.py show` to verify your configuration is saved correctly.

**Issue**: Old paths still being used
**Solution**: Make sure all scripts have been updated to the latest version.

## Technical Details

The configuration system consists of:

1. **config.json** - Stores user preferences
2. **config.py** - Python module for reading/writing config
3. **configure.py** - User-friendly configuration tool
4. **get_config_value.py** - Helper for batch files to read config

All paths are automatically derived from the model ID, ensuring consistency across the entire pipeline.
