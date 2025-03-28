import requests
import json

register_url = "http://localhost:8000/register_function"
register_payload = {
    "name": "say_hello",
    "description": "Prints a hello message to the console",
    "params": ["message"]
}
response = requests.post(register_url, json=register_payload)
print("Register Response:", response.json())

execute_url = "http://localhost:8000/execute"
prompts = [
    "Say hello to the world",
    "Say it again"
]

for prompt in prompts:
    payload = {"prompt": prompt}
    response = requests.post(execute_url, json=payload)
    data = response.json()
    print(f"Prompt: {prompt}")
    print(f"Function: {data['function']}")
    print("Generated Code:")
    print(data['code'])
    print("-" * 50)
