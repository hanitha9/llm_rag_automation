# LLM RAG Automation API

## Project Overview
The **LLM RAG Automation API** is a Python-based system that utilizes a Retrieval-Augmented Generation (RAG) approach to interpret natural language prompts and automate tasks. It retrieves functions from a registry, generates executable Python code, and maintains session context, all served via a FastAPI endpoint. Built as an intern task assignment, this project demonstrates automation capabilities with additional features like logging and custom function support.

### Objectives
- Convert natural language commands into actionable Python scripts.
- Demonstrate RAG-based function retrieval, context awareness, and dynamic code generation.
- Provide an extensible, user-friendly API with monitoring capabilities.

### Core Requirements
1. **Function Registry:** Predefined functions for app control, system monitoring, and command execution.
2. **LLM + RAG Retrieval:** Utilize a RAG engine to match prompts to functions via vector similarity.
3. **Dynamic Code Generation:** Generate executable Python code with error handling.
4. **Maintain Context:** Preserve session history for follow-up prompts (e.g., "Show it again").
5. **API Service:** FastAPI endpoint (`/execute`) to process prompts and return responses.

### Bonus Features
1. **Logging and Monitoring:** Log execution details to `api_execution.log` and provide a `/monitor` endpoint.
2. **Custom Functions:** Allow users to register new functions via `/register_function`.

---

## Project Structure
```
llm_rag_automation/
├── api_service.py           # FastAPI service with endpoints
├── automation_functions.py  # Function registry
├── code_generator.py        # Code generation logic
├── rag_engine.py            # RAG retrieval with context
├── test_client.py           # Core functionality test
├── test_client1.py          # Context awareness test
├── test_custom.py           # Custom function test
├── test_open_calculator.py  # Individual execution test
├── test_open_chrome.py      # Individual execution test
├── test_get_cpu_usage.py    # Individual execution test
├── test_create_text_file.py # Individual execution test
├── test_run_shell_command.py# Individual execution test
├── requirements.txt         # Dependencies
├── api_execution.log        # Execution logs (generated)
├── screenshots/             # Output screenshots
│   ├── test_client_output.png
│   ├── test_client1_output.png
│   ├── test_custom_output.png
│   ├── execution_logs.png
│   └── example_txt_created.png
└── README.md                # This file
```

---

## Setup Instructions

### Prerequisites
- **Python 3.10+**: Installed and accessible via command line.
- **Git**: For cloning the repository.
- **Windows OS**: Functions are Windows-specific (e.g., `calc.exe`, `dir`).

### Step-by-Step Setup
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/llm_rag_automation.git
   cd llm_rag_automation
   ```
2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # For Windows
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the API:**
   ```bash
   python api_service.py
   ```
   - Output: Uvicorn running on `http://0.0.0.0:8000`.
   - Keep this terminal open.

---

## How It Works

### Components
1. **Function Registry (`automation_functions.py`)**
   - Contains predefined functions:
     - `open_calculator()`: Opens Windows Calculator.
     - `open_chrome()`: Launches Google Chrome.
     - `get_cpu_usage()`: Retrieves CPU usage percentage.
     - `create_text_file(filename)`: Creates a text file.
     - `run_shell_command(command)`: Runs a shell command (e.g., `dir`).

2. **RAG Engine (`rag_engine.py`)**
   - Uses `sentence-transformers` to encode function descriptions into vectors.
   - FAISS index for similarity search.
   - Maintains context for follow-ups.

3. **Code Generator (`code_generator.py`)**
   - Generates Python scripts with imports, function calls, and error handling.
   - Example: `create_text_file('example.txt')` → full script with `try-except`.

4. **API Service (`api_service.py`)**
   - Endpoints:
     - `POST /execute`: Processes prompts, returns function and code.
     - `GET /monitor`: Returns last 10 execution logs.
     - `POST /register_function`: Registers custom functions.
   - Maintains `chat_history` for context.
   - Logs execution details to `api_execution.log`.

---

## Running Tests

### Core Functionality Test (`test_client.py`)
```bash
python test_client.py
```
- Expected Output:
  ```
  Prompt: Open calculator -> 'open_calculator'
  Prompt: Launch Google Chrome -> 'open_chrome'
  Prompt: Check CPU usage -> 'get_cpu_usage'
  ```

### Context Awareness Test (`test_client1.py`)
```bash
python test_client1.py
```
- Expected Output:
  ```
  Prompt: Check CPU usage -> 'get_cpu_usage'
  Prompt: Show it again -> 'get_cpu_usage'
  ```

### Custom Function Test (`test_custom.py`)
```bash
python test_custom.py
```
- Expected Output:
  ```
  Register Response: {'message': "Function 'say_hello' registered successfully"}
  ```

### Individual Execution Tests
```bash
python test_open_calculator.py
python test_open_chrome.py
python test_get_cpu_usage.py
python test_create_text_file.py
python test_run_shell_command.py
```

---

## Additional Features

### Logging
- File: `api_execution.log`
- Logs prompt receipt, function retrieval, and errors.

### Monitoring
- Endpoint: `GET /monitor`
- Fetch logs via:
  ```python
  import requests
  print(requests.get("http://localhost:8000/monitor").json())
  ```

---

## Troubleshooting

| Issue | Solution |
|--------|----------|
| API not starting | Check dependencies (`pip install -r requirements.txt`). Ensure port 8000 is free (`netstat -aon | findstr 8000`). |
| Test failures | Verify `api_service.py` is running. Check function implementations. |
| Custom function not retrieved | Ensure successful registration. Verify RAG index rebuild. |
| Execution errors | Confirm Windows-specific commands. Check file permissions. |

---
## screen recordings
   ###Core Functionality,Context Awareness,Custom Function testing    
    ![Recording 2025-03-28 212325](https://github.com/user-attachments/assets/0d92f24e-2042-4a59-807c-aff10d290329)
   ###individual execution tests
    ![Recording 2025-03-28 212056](https://github.com/user-attachments/assets/ad761a38-cc92-4fd8-91a2-02aa0934427b)

## Submission Details
- **GitHub**: https://github.com/yourusername/llm_rag_automation
- **Author**: Hanitha
- **Date**: March 28, 2025

Clone, run, and explore—everything you need is here! 🚀

