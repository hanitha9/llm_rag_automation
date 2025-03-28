import requests
import json

url = "http://localhost:8000/execute"
prompts = [
    "Check CPU usage",
    "Show it again",
    "Create a text file"
]

for prompt in prompts:
    payload = {"prompt": prompt}
    response = requests.post(url, json=payload)
    data = response.json()
    print(f"Prompt: {prompt}")
    print(f"Function: {data['function']}")
    print("Generated Code:")
    print(data['code'])
    print("-" * 50)
