import requests
import json

url = "http://127.0.0.1:11434/api/chat"

payload = {
    "model": "llama3.1:8b",
    "messages": [{"role": "user", "content": "what is python?"}]
}

response = requests.post(url, json=payload, stream=True)

if response.status_code == 200:
    print("Streaming response from Ollama:")
    for line in response.iter_lines(decode_unicode=True):
        if line:
            try:
                json_data = json.loads(line)
                if "message" in json_data and "content" in json_data["message"]:
                    print(json_data["message"]["content"], end="")
            except json.JSONDecodeError:
                print(f"\nFailed to parse line: {line}")
    print()
else:
    print(f"Error: {response.status_code}")
    print(response.text)
