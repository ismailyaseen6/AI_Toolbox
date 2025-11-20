from huggingface_hub import snapshot_download

model_id = "google/gemma-3-1b-it"
snapshot_download(repo_id= model_id, local_dir="./Outputs/gemma-3-1b-it", local_dir_use_symlinks=False, revision="main")