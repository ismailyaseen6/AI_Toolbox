# Quick Start Guide - Configurable AI_Toolbox

## 🎯 What's New?

Your AI_Toolbox is now **fully configurable**! Switch between any HuggingFace model with a single command.

## 📋 First Time Setup

### Step 1: Configure Your Model
```bash
python configure.py set google/gemma-3-1b-it
```

### Step 2: Run Initial Setup
```bash
setup.bat
```

### Step 3: Run the Pipeline
```bash
Run.bat
```

Done! Your model is now fine-tuned and converted to GGUF format.

## 🔄 Switching Models

Want to try a different model? It's easy:

```bash
# Try Mistral
python configure.py set mistralai/Mistral-7B-v0.1

# Run the pipeline with the new model
Run.bat
```

## 🎨 User-Friendly Interface

Prefer a menu? Use the batch file:

```bash
configure.bat
```

This will show you a menu with popular models to choose from.

## 📊 Check Your Configuration

```bash
python configure.py show
```

Output:
```
============================================================
CURRENT CONFIGURATION
============================================================
Model ID: google/gemma-3-1b-it
Dataset: databricks/databricks-dolly-15k

Derived Configuration:
  Model Name: gemma-3-1b-it
  Base Model Directory: ./Outputs/gemma-3-1b-it
  Fine-tuned Directory: ./Outputs/fine-tuned-gemma-3-1b-it-yaseen
  GGUF Filename: gemma-3-1b-it-yaseen.gguf
  Ollama Model Name: gemma-3-1b-it-yaseen
============================================================
```

## 🚀 Popular Models to Try

| Model | Command |
|-------|---------|
| Gemma 3 1B | `python configure.py set google/gemma-3-1b-it` |
| Gemma 2 2B | `python configure.py set google/gemma-2-2b-it` |
| Phi-2 | `python configure.py set microsoft/phi-2` |
| Mistral 7B | `python configure.py set mistralai/Mistral-7B-v0.1` |
| Llama 2 7B | `python configure.py set meta-llama/Llama-2-7b-chat-hf` |
| TinyLlama | `python configure.py set TinyLlama/TinyLlama-1.1B-Chat-v1.0` |

## ❓ Interactive Mode

Just run without arguments for an interactive prompt:

```bash
python configure.py
```

## 📝 Advanced: Custom Dataset

```bash
python configure.py set google/gemma-3-1b-it your-org/your-dataset
```

## 🔧 How It Works

1. You set a HuggingFace model ID (e.g., `google/gemma-3-1b-it`)
2. The system automatically generates all paths and names
3. All scripts read from the central configuration
4. Everything stays synchronized - no manual editing needed!

## 💡 Tips

- You can switch models anytime - just run `configure.py` again
- The configuration persists across runs
- All existing batch files (`setup.bat`, `Run.bat`) work the same way
- Model files are saved in `Outputs/` with the model name

## 📚 More Information

- [CONFIGURATION.md](CONFIGURATION.md) - Detailed configuration guide
- [IMPLEMENTATION_SUMMARY.md](IMPLEMENTATION_SUMMARY.md) - Technical details
- [README.md](README.md) - Main documentation

## 🎉 That's It!

You now have a fully configurable AI pipeline. Experiment with different models and see which one works best for your use case!
