# automation_functions.py
import os
import webbrowser
import psutil
import subprocess

# Application Control Functions
def open_chrome():
    webbrowser.open("https://www.google.com")

def open_calculator():
    os.system("calc" if os.name == 'nt' else "gnome-calculator")

def open_notepad():
    os.system("notepad" if os.name == 'nt' else "gedit")

# System Monitoring Functions
def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

# Command Execution Functions
def run_shell_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout

# Additional Utility Functions
def create_text_file(filename):
    with open(filename, 'w') as f:
        f.write("New file created")

# Function metadata for RAG
FUNCTION_METADATA = {
    "open_chrome": {"description": "Launches the Google Chrome web browser to a default page"},
    "open_calculator": {"description": "Starts the system calculator application"},
    "open_notepad": {"description": "Opens the Notepad text editor"},
    "get_cpu_usage": {"description": "Measures and returns the current CPU utilization percentage"},
    "get_ram_usage": {"description": "Measures and returns the current RAM utilization percentage"},
    "run_shell_command": {"description": "Executes a specified command in the system shell", "params": ["command"]},
    "create_text_file": {"description": "Generates a new text file with a given name", "params": ["filename"]}
}
