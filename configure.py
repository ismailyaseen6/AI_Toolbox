"""
Configuration Manager for AI_Toolbox
Simple script to configure the HuggingFace model to use
"""
import sys
from config import save_config, get_model_config
import json

def display_current_config():
    """Display the current configuration"""
    print("\n" + "="*60)
    print("CURRENT CONFIGURATION")
    print("="*60)
    cfg = get_model_config()
    print(f"Model ID: {cfg['model_id']}")
    print(f"Dataset: {cfg['dataset_name']}")
    print(f"\nDerived Configuration:")
    print(f"  Model Name: {cfg['model_name']}")
    print(f"  Base Model Directory: {cfg['base_model_dir']}")
    print(f"  Fine-tuned Directory: {cfg['fine_tuned_dir']}")
    print(f"  GGUF Filename: {cfg['gguf_filename']}")
    print(f"  Ollama Model Name: {cfg['ollama_model_name']}")
    print("="*60 + "\n")

def interactive_config():
    """Interactive configuration"""
    print("\n" + "="*60)
    print("AI_TOOLBOX CONFIGURATION")
    print("="*60)
    
    try:
        cfg = get_model_config()
        print(f"\nCurrent Model ID: {cfg['model_id']}")
        print(f"Current Dataset: {cfg['dataset_name']}")
    except:
        print("\nNo existing configuration found.")
    
    print("\nEnter the HuggingFace model ID (e.g., google/gemma-3-1b-it)")
    print("Press Enter to keep current value or Ctrl+C to cancel")
    
    model_id = input("\nModel ID: ").strip()
    
    if not model_id:
        print("No changes made.")
        return
    
    print("\nEnter the dataset name (optional, press Enter for default)")
    print("Default: databricks/databricks-dolly-15k")
    dataset = input("\nDataset: ").strip()
    
    # Save configuration
    save_config(model_id, dataset if dataset else None)
    
    print("\n" + "="*60)
    print("CONFIGURATION SAVED SUCCESSFULLY!")
    print("="*60)
    
    # Show the new configuration
    display_current_config()

def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == "show" or command == "view" or command == "display":
            display_current_config()
        
        elif command == "set":
            if len(sys.argv) < 3:
                print("Usage: python configure.py set <model_id> [dataset_name]")
                print("Example: python configure.py set google/gemma-3-1b-it")
                sys.exit(1)
            
            model_id = sys.argv[2]
            dataset = sys.argv[3] if len(sys.argv) > 3 else None
            save_config(model_id, dataset)
            display_current_config()
        
        elif command == "help" or command == "-h" or command == "--help":
            print("\nAI_Toolbox Configuration Manager")
            print("\nUsage:")
            print("  python configure.py              - Interactive configuration")
            print("  python configure.py show         - Display current configuration")
            print("  python configure.py set <model>  - Set model ID directly")
            print("  python configure.py help         - Show this help")
            print("\nExamples:")
            print("  python configure.py set google/gemma-3-1b-it")
            print("  python configure.py set meta-llama/Llama-2-7b-hf")
            print("  python configure.py set mistralai/Mistral-7B-v0.1")
            print()
        
        else:
            print(f"Unknown command: {command}")
            print("Run 'python configure.py help' for usage information")
    
    else:
        # No arguments - run interactive mode
        interactive_config()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nConfiguration cancelled.")
        sys.exit(0)
