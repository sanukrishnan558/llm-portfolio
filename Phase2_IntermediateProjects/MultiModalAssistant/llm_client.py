import os
import requests

class LLMClient:
    def __init__(self, model="llama3"):
        self.model = model
        self.ollama_url = os.environ.get("OLLAMA_URL", "http://localhost:11434")

    def generate(self, prompt):
        """Send a prompt to the Ollama server and return the response text."""
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False
        }
        response = requests.post(f"{self.ollama_url}/api/generate", json=payload)
        if response.status_code != 200:
            raise RuntimeError(f"Ollama request failed: {response.text}")

        data = response.json()
        return data.get("response", "").strip()
