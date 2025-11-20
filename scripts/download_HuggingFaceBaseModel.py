from huggingface_hub import snapshot_download
import sys
import os

# Add parent directory to path to import config
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from config import get_model_config

cfg = get_model_config()
print(f"Downloading model: {cfg['model_id']}")
print(f"Target directory: {cfg['base_model_dir']}")
snapshot_download(repo_id=cfg['model_id'], local_dir=cfg['base_model_dir'], local_dir_use_symlinks=False, revision="main")