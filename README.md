# AI Toolbox

A collection of tools for fine-tuning, converting, and running language models.

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

### Initial Setup
```bash
setup.bat
```

### Full Pipeline (Fine-tune → Merge → Convert)
```bash
Run.bat
```

### Import to Ollama
```bash
ollamaImportGGUF.bat
```

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
