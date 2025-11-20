"""
Helper script to output config values for batch files
Usage: python get_config_value.py <key>
"""
import sys
from config import get_model_config

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python get_config_value.py <key>")
        sys.exit(1)
    
    cfg = get_model_config()
    key = sys.argv[1]
    
    if key in cfg:
        print(cfg[key], end='')
    else:
        print(f"Error: Key '{key}' not found in config", file=sys.stderr)
        sys.exit(1)
