import requests
import json

url = "http://localhost:8000/execute"
prompts = [
    "Open calculator",
    "Launch Google Chrome",
    "Check CPU usage",
    "Create a text file",
    "Run a command"
]

for prompt in prompts:
    payload = {"prompt": prompt}
    response = requests.post(url, json=payload)
    data = response.json()
    print(f"Prompt: {prompt}")
    print(f"Function: {data['function']}")
    print("Generated Code:")
    print(data['code'])  # Directly print the code string with proper newlines
    print("-" * 50)
