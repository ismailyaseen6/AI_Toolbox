from flask import Flask, render_template, jsonify, Response, request
import subprocess
import threading
import time
import os
import queue
from config import get_model_config, save_config

app = Flask(__name__)

# Global variables for tracking progress
progress_queue = queue.Queue()
current_process = None
is_running = False

def run_batch_file(batch_file, step_name):
    """Run a batch file and capture output"""
    global current_process
    try:
        progress_queue.put({
            'step': step_name,
            'status': 'running',
            'message': f'Starting {step_name}...',
            'output': f'Starting {step_name}...'
        })
        
        # Run the batch file
        current_process = subprocess.Popen(
            [batch_file],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
            universal_newlines=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        # Stream output
        for line in current_process.stdout:
            progress_queue.put({
                'step': step_name,
                'status': 'running',
                'message': '',
                'output': line.strip()
            })
        
        current_process.wait()
        
        if current_process.returncode == 0:
            progress_queue.put({
                'step': step_name,
                'status': 'completed',
                'message': f'{step_name} completed successfully',
                'output': f'{step_name} completed successfully'
            })
            return True
        else:
            progress_queue.put({
                'step': step_name,
                'status': 'error',
                'message': f'{step_name} failed with error code {current_process.returncode}',
                'output': f'{step_name} failed with error code {current_process.returncode}'
            })
            return False
    except Exception as e:
        progress_queue.put({
            'step': step_name,
            'status': 'error',
            'message': f'Error running {step_name}: {str(e)}',
            'output': ''
        })
        return False

def execute_pipeline():
    """Execute setup.bat and run.bat in sequence"""
    global is_running
    is_running = True
    
    try:
        # Step 1: Run setup.bat
        if not run_batch_file('setup.bat', 'Setup'):
            progress_queue.put({
                'step': 'Pipeline',
                'status': 'error',
                'message': 'Pipeline stopped due to setup failure',
                'output': '',
                'finished': True
            })
            is_running = False
            return
        
        # Step 2: Run Run.bat
        if not run_batch_file('Run.bat', 'Execution'):
            progress_queue.put({
                'step': 'Pipeline',
                'status': 'error',
                'message': 'Pipeline stopped due to execution failure',
                'output': '',
                'finished': True
            })
            is_running = False
            return
        
        # All steps completed
        progress_queue.put({
            'step': 'Pipeline',
            'status': 'completed',
            'message': 'All steps completed successfully!',
            'output': '',
            'finished': True
        })
    except Exception as e:
        progress_queue.put({
            'step': 'Pipeline',
            'status': 'error',
            'message': f'Pipeline error: {str(e)}',
            'output': '',
            'finished': True
        })
    finally:
        is_running = False

@app.route('/')
def index():
    """Main page"""
    cfg = get_model_config()
    return render_template('launcher.html', config=cfg)

@app.route('/config', methods=['GET'])
def get_config():
    """Get current configuration"""
    try:
        cfg = get_model_config()
        return jsonify(cfg)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/config', methods=['POST'])
def update_config():
    """Update configuration"""
    try:
        data = request.json
        model_id = data.get('model_id')
        dataset_name = data.get('dataset_name')
        
        if not model_id:
            return jsonify({'error': 'model_id is required'}), 400
        
        save_config(model_id, dataset_name)
        cfg = get_model_config()
        return jsonify({'message': 'Configuration updated', 'config': cfg})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/start', methods=['POST'])
def start_pipeline():
    """Start the batch file pipeline"""
    global is_running
    
    if is_running:
        return jsonify({'error': 'Pipeline is already running'}), 400
    
    # Clear the queue
    while not progress_queue.empty():
        progress_queue.get()
    
    # Start the pipeline in a background thread
    thread = threading.Thread(target=execute_pipeline)
    thread.daemon = True
    thread.start()
    
    return jsonify({'message': 'Pipeline started'})

@app.route('/stop', methods=['POST'])
def stop_pipeline():
    """Stop the current pipeline"""
    global current_process, is_running
    
    if current_process and current_process.poll() is None:
        current_process.terminate()
        progress_queue.put({
            'step': 'Pipeline',
            'status': 'stopped',
            'message': 'Pipeline stopped by user',
            'output': '',
            'finished': True
        })
        is_running = False
        return jsonify({'message': 'Pipeline stopped'})
    
    return jsonify({'error': 'No pipeline is currently running'}), 400

@app.route('/progress')
def stream_progress():
    """Stream progress updates to the client"""
    def generate():
        while True:
            try:
                # Get progress update with timeout
                update = progress_queue.get(timeout=1)
                yield f"data: {str(update)}\n\n"
                
                # Check if pipeline is finished
                if update.get('finished'):
                    break
            except queue.Empty:
                # Send heartbeat to keep connection alive
                yield f"data: {{'heartbeat': true}}\n\n"
    
    return Response(generate(), mimetype='text/event-stream')

@app.route('/status')
def get_status():
    """Get current pipeline status"""
    return jsonify({'is_running': is_running})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001, threaded=True)
