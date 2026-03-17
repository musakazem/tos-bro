import requests

from config import (
    OPENROUTER_BASE_URL,
    OPENROUTER_MODEL,
    OPENROUTER_TOKEN,
)

class OpenRouter:
    def __init__(self, instructions=None):
        self.base_url = OPENROUTER_BASE_URL
        self.token = OPENROUTER_TOKEN
        self.model = OPENROUTER_MODEL

        self.instructions = instructions

    @property
    def connection_config(self):
        return {
            "url": self.base_url,
            "headers": {"Authorization": f"Bearer {self.token}"},
        }

    def _get_messages(self, message):
        messages = []
        if self.instructions:
            messages.append({"role": "system", "content": self.instructions})
        messages.append({"role": "user", "content": message})
        return messages

    def prompt(self, message):
        config = self.connection_config

        config["json"] = {
            "model": self.model,
            "messages": self._get_messages(message)
        }

        response = requests.post(**config)

        try:
            content = response.json()
            return f"{content['choices'][0]['message']['content']} \n \n AI model: {content['model']}"

        except Exception as e:
            print(f"OpenRouter Error: {e}: {response.text}")
            return None