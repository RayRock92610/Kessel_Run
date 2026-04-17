import time
import json
import os

class InquisitorEngine:
    """
    Core Logic for Inquisitor v8.0
    Focus: Constant Learning & Error Log Management
    """
    def __init__(self):
        self.memory_buffer = []
        self.error_log = "error_v8_0.log"
        self.correction_log = "corrections_v8_0.json"
        
        # Ensure the correction log exists so we don't get FileNotFoundError on first run
        if not os.path.exists(self.correction_log):
            with open(self.correction_log, 'w') as f:
                json.dump({}, f)

    def active_recall(self, task_key):
        with open(self.correction_log, 'r') as f:
            corrections = json.load(f)
            return corrections.get(task_key, "No prior patterns found.")

    def log_failure(self, task, error):
        entry = {
            "timestamp": time.time(),
            "task": task,
            "error": str(error),
            "status": "Awaiting Correction"
        }
        with open(self.error_log, "a") as f:
            f.write(f"{json.dumps(entry)}\n")
        print(f"[*] Inquisitor v8.0: Failure logged. Self-repair initiated.")

# Initialize Architecture and test the logging mechanism
engine = InquisitorEngine()
print("[*] Inquisitor v8.0 Initialized successfully.")
engine.log_failure("Terminal Execution", "Bash attempted to parse Python syntax.")
