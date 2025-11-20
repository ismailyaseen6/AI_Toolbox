# 🎯 AI_Toolbox Configuration System - Complete Guide

## ✨ Overview

Your AI_Toolbox now features a **centralized configuration system** that allows you to switch between any HuggingFace model with a single command. No more manually editing multiple files!

---

## 🚀 Quick Commands

```bash
# Set a model
python configure.py set google/gemma-3-1b-it

# Interactive configuration
python configure.py

# View current settings
python configure.py show

# Windows menu
configure.bat
```

---

## 📦 What's Included

### New Files
- **config.json** - Your model configuration
- **config.py** - Configuration module
- **configure.py** - Configuration tool (Python)
- **configure.bat** - Configuration tool (Windows)
- **get_config_value.py** - Helper for batch files
- **verify_config.py** - Test the configuration system
- **CONFIGURATION.md** - Full documentation
- **QUICKSTART.md** - Quick start guide
- **IMPLEMENTATION_SUMMARY.md** - Technical details

### Modified Files
All scripts now automatically read from `config.json`:
- ✅ `scripts/download_HuggingFaceBaseModel.py`
- ✅ `scripts/fineTune_HuggingFaceModel.py`
- ✅ `scripts/modelToGGUF_part1.py`
- ✅ `scripts/run_LocalModel.py`
- ✅ `scripts/run_Transformers_Huggingface.py`
- ✅ `scripts/modelToGGUF_part2.bat`
- ✅ `scripts/ollamaImportGGUF.bat`

---

## 📋 Usage Examples

### Example 1: First Time Setup
```bash
# Configure model
python configure.py set google/gemma-3-1b-it

# Install dependencies
setup.bat

# Run pipeline
Run.bat
```

### Example 2: Switch Models
```bash
# Switch to Mistral
python configure.py set mistralai/Mistral-7B-v0.1

# Run with new model
Run.bat
```

### Example 3: Try Different Models
```bash
# Try Phi-2
python configure.py set microsoft/phi-2
Run.bat

# Try Llama 2
python configure.py set meta-llama/Llama-2-7b-chat-hf
Run.bat

# Back to Gemma
python configure.py set google/gemma-3-1b-it
Run.bat
```

---

## 🎨 Interactive Mode

### Python Interactive
```bash
python configure.py
```

Example session:
```
============================================================
AI_TOOLBOX CONFIGURATION
============================================================

Current Model ID: google/gemma-3-1b-it
Current Dataset: databricks/databricks-dolly-15k

Enter the HuggingFace model ID (e.g., google/gemma-3-1b-it)
Press Enter to keep current value or Ctrl+C to cancel

Model ID: microsoft/phi-2

Enter the dataset name (optional, press Enter for default)
Default: databricks/databricks-dolly-15k

Dataset: 

============================================================
CONFIGURATION SAVED SUCCESSFULLY!
============================================================
```

### Windows Batch Menu
```bash
configure.bat
```

Shows a user-friendly menu:
```
============================================
AI_TOOLBOX MODEL CONFIGURATION
============================================

Current Configuration:
[shows current config]

============================================
Would you like to change the model?
============================================

Popular models:
  1. google/gemma-3-1b-it
  2. microsoft/phi-2
  3. mistralai/Mistral-7B-v0.1
  4. meta-llama/Llama-2-7b-chat-hf
  5. TinyLlama/TinyLlama-1.1B-Chat-v1.0
  6. Custom model ID
  7. Keep current configuration

Enter your choice (1-7):
```

---

## 🎯 How It Works

### Simple Flow
1. **You configure**: Set HuggingFace model ID
2. **System generates**: All paths, filenames, and names automatically
3. **Scripts use**: All scripts read from central config
4. **Stay synchronized**: Everything always matches

### Example Configuration
Input: `google/gemma-3-1b-it`

Automatically generates:
```
Model Name: gemma-3-1b-it
Base Directory: ./Outputs/gemma-3-1b-it
Fine-tuned: ./Outputs/fine-tuned-gemma-3-1b-it-yaseen
GGUF: gemma-3-1b-it-yaseen.gguf
Ollama: gemma-3-1b-it-yaseen
```

---

## 🔧 Verification

Test that everything works:

```bash
python verify_config.py
```

Should show:
```
✅ Config module imports successfully
✅ Config loaded: google/gemma-3-1b-it
✅ All required config keys present
✅ Helper script works
✅ All scripts import config correctly

🎉 All tests passed!
```

---

## 📚 Popular Models

| Model | Size | Command |
|-------|------|---------|
| Gemma 3 1B IT | 1B | `python configure.py set google/gemma-3-1b-it` |
| Gemma 2 2B IT | 2B | `python configure.py set google/gemma-2-2b-it` |
| Phi-2 | 2.7B | `python configure.py set microsoft/phi-2` |
| TinyLlama | 1.1B | `python configure.py set TinyLlama/TinyLlama-1.1B-Chat-v1.0` |
| Mistral 7B | 7B | `python configure.py set mistralai/Mistral-7B-v0.1` |
| Mistral Instruct | 7B | `python configure.py set mistralai/Mistral-7B-Instruct-v0.2` |
| Llama 2 Chat | 7B | `python configure.py set meta-llama/Llama-2-7b-chat-hf` |
| Llama 2 | 7B | `python configure.py set meta-llama/Llama-2-7b-hf` |

---

## 💡 Tips & Best Practices

### ✅ Do's
- ✅ Use `configure.py` to change models
- ✅ Run `verify_config.py` if something seems wrong
- ✅ Check `configure.py show` to see current config
- ✅ Use the interactive mode if unsure

### ❌ Don'ts
- ❌ Don't manually edit scripts with model names
- ❌ Don't hardcode paths in custom scripts
- ❌ Don't edit `config.json` directly (use `configure.py`)

### 🎓 Advanced Usage
Import config in your own scripts:
```python
from config import get_model_config

cfg = get_model_config()
print(f"Using model: {cfg['model_id']}")
print(f"Output path: {cfg['base_model_dir']}")
```

---

## 🐛 Troubleshooting

### Problem: Scripts can't find config module
**Solution**: Run from project root directory
```bash
cd C:\Users\ismai\Documents\AI_Toolbox
python configure.py
```

### Problem: Old model name still appears
**Solution**: Verify configuration was saved
```bash
python configure.py show
```

### Problem: Batch files show wrong paths
**Solution**: Run verification
```bash
python verify_config.py
```

---

## 📖 Documentation Files

- **README.md** - Main project documentation
- **QUICKSTART.md** - Quick start guide (this file)
- **CONFIGURATION.md** - Detailed configuration guide
- **IMPLEMENTATION_SUMMARY.md** - Technical implementation details

---

## 🎉 Summary

You now have a **fully configurable AI pipeline**:

1. ⚙️ **Easy configuration** - One command to change models
2. 🔄 **Automatic paths** - Everything derived automatically  
3. 🎯 **Consistent naming** - All files follow same pattern
4. ✅ **Verified working** - All tests pass
5. 📚 **Well documented** - Multiple guides available

**Start experimenting with different models today!** 🚀

```bash
python configure.py set <your-favorite-model>
Run.bat
```
