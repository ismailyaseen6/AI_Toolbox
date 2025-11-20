"""
Verification test for the configuration system
Run this to verify everything is working correctly
"""
import sys
import os
from pathlib import Path

def test_config_module():
    """Test that config module loads and works"""
    print("Testing config module...")
    try:
        from config import get_model_config, load_config, save_config
        print("✅ Config module imports successfully")
        return True
    except Exception as e:
        print(f"❌ Config module import failed: {e}")
        return False

def test_config_loading():
    """Test that config loads"""
    print("\nTesting config loading...")
    try:
        from config import get_model_config
        cfg = get_model_config()
        print(f"✅ Config loaded: {cfg['model_id']}")
        return True
    except Exception as e:
        print(f"❌ Config loading failed: {e}")
        return False

def test_config_values():
    """Test that all expected config values exist"""
    print("\nTesting config values...")
    try:
        from config import get_model_config
        cfg = get_model_config()
        required_keys = [
            'model_id', 'model_name', 'dataset_name',
            'base_model_dir', 'fine_tuned_dir', 'merged_model_dir',
            'gguf_filename', 'gguf_path', 'ollama_model_name'
        ]
        
        missing_keys = [key for key in required_keys if key not in cfg]
        if missing_keys:
            print(f"❌ Missing keys: {missing_keys}")
            return False
        
        print("✅ All required config keys present")
        for key in required_keys:
            print(f"   {key}: {cfg[key]}")
        return True
    except Exception as e:
        print(f"❌ Config values test failed: {e}")
        return False

def test_helper_script():
    """Test that get_config_value.py works"""
    print("\nTesting helper script...")
    try:
        import subprocess
        result = subprocess.run(
            ['python', 'get_config_value.py', 'model_id'],
            capture_output=True,
            text=True
        )
        if result.returncode == 0:
            print(f"✅ Helper script works: {result.stdout}")
            return True
        else:
            print(f"❌ Helper script failed: {result.stderr}")
            return False
    except Exception as e:
        print(f"❌ Helper script test failed: {e}")
        return False

def test_scripts_import_config():
    """Test that scripts can import config"""
    print("\nTesting script imports...")
    scripts_dir = Path('scripts')
    
    test_scripts = [
        'download_HuggingFaceBaseModel.py',
        'fineTune_HuggingFaceModel.py',
        'modelToGGUF_part1.py',
        'run_LocalModel.py',
        'run_Transformers_Huggingface.py'
    ]
    
    all_passed = True
    for script in test_scripts:
        script_path = scripts_dir / script
        if not script_path.exists():
            print(f"⚠️  Script not found: {script}")
            continue
        
        try:
            # Read script and check for config import
            content = script_path.read_text()
            if 'from config import get_model_config' in content:
                print(f"✅ {script} imports config correctly")
            else:
                print(f"❌ {script} doesn't import config")
                all_passed = False
        except Exception as e:
            print(f"❌ Error checking {script}: {e}")
            all_passed = False
    
    return all_passed

def main():
    print("="*60)
    print("AI_TOOLBOX CONFIGURATION SYSTEM VERIFICATION")
    print("="*60)
    
    tests = [
        test_config_module,
        test_config_loading,
        test_config_values,
        test_helper_script,
        test_scripts_import_config
    ]
    
    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"❌ Test failed with exception: {e}")
            results.append(False)
    
    print("\n" + "="*60)
    print("SUMMARY")
    print("="*60)
    passed = sum(results)
    total = len(results)
    print(f"Tests passed: {passed}/{total}")
    
    if all(results):
        print("\n🎉 All tests passed! Configuration system is working correctly.")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please check the errors above.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
