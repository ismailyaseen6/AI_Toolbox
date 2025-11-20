# AI Toolbox

A collection of tools for fine-tuning, converting, and running language models.

## 🚀 Quick Configuration

**NEW: Easily switch between any HuggingFace model!**

```bash
# Configure your model
python configure.py set google/gemma-3-1b-it

# Or use interactive mode
python configure.py

# View current configuration
python configure.py show
```

All scripts automatically use your configured model. See [CONFIGURATION.md](CONFIGURATION.md) for details.

## Installation

### Clone the Repository (with submodules)
```bash
git clone --recursive https://github.com/ismailyaseen6/AI_Toolbox.git
cd AI_Toolbox
```

Or if you already cloned without `--recursive`:
```bash
git submodule update --init --recursive
```

### Setup Environment
```bash
setup.bat
```

This will:
- Create a Python virtual environment
- Install all required dependencies including PyTorch with CUDA support
- Initialize the llama.cpp submodule

## Project Structure

```
AI_Toolbox/
├── scripts/                          # Python scripts for model operations
│   ├── download_HuggingFaceBaseModel.py    # Download base models from HuggingFace
│   ├── fineTune_HuggingFaceModel.py        # Fine-tune models with LoRA
│   ├── modelToGGUF_part1.py                # Merge LoRA weights with base model
│   ├── run_LocalModel.py                   # Run local models with transformers
│   └── run_Transformers_Huggingface.py     # Run HuggingFace models directly
│
├── Run.bat                           # Main workflow: fine-tune → merge → convert to GGUF
├── setup.bat                         # Setup environment and download dependencies
├── modelToGGUF_part2.bat            # Convert merged model to GGUF format
├── ollamaImportGGUF.bat             # Import GGUF models into Ollama
│
├── Outputs/                          # Model outputs and conversions
│   ├── gemma-3-1b-it/               # Base model
│   ├── fine-tuned-gemma-3-1b-it-yaseen/  # Fine-tuned model with LoRA
│   ├── merged-model/                # Merged model (LoRA + base)
│   └── gemma-3-1b-it-yaseen.gguf   # Final GGUF file
│
├── llama.cpp/                        # llama.cpp repository for GGUF conversion
├── requirements.txt                  # Python dependencies
└── .venv/                           # Python virtual environment
```

## Quick Start

### 1. Configure Your Model
```bash
# Set your HuggingFace model
python configure.py set google/gemma-3-1b-it

# Or try another model
python configure.py set mistralai/Mistral-7B-v0.1
```

### 2. Initial Setup
```bash
setup.bat
```

### 3. Full Pipeline (Fine-tune → Merge → Convert)
```bash
Run.bat
```

### 4. Import to Ollama
```bash
ollamaImportGGUF.bat
```

**Note**: You can change the model at any time by running `python configure.py` again!

## Scripts

### Model Download
- **download_HuggingFaceBaseModel.py**: Downloads base models from HuggingFace Hub

### Fine-tuning
- **fineTune_HuggingFaceModel.py**: Fine-tunes models using LoRA (Low-Rank Adaptation)

### Model Conversion
- **modelToGGUF_part1.py**: Merges LoRA weights with base model
- **modelToGGUF_part2.bat**: Converts merged model to GGUF format using llama.cpp

### Model Inference
- **run_LocalModel.py**: Run locally saved models
- **run_Transformers_Huggingface.py**: Run models directly from HuggingFace

### Ollama Integration
- **ollamaImportGGUF.bat**: Import GGUF models into Ollama for easy deployment

## Requirements

- Python 3.10+
- CUDA-capable GPU (recommended for fine-tuning)
- Git
- Ollama (optional, for model deployment)

## Notes

- All Python scripts are located in the `scripts/` folder
- Model outputs are saved in the `Outputs/` folder
- The batch files automatically reference scripts in their new locations
