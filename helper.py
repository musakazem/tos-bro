import ollama


class AIModel:
    def __init__(self, model: str, instructions: str = None):
        self.model = model
        self.instructions = instructions

    def prompt(self, message: str) -> str:
        messages = []

        if self.instructions:
            messages.append({"role": "system", "content": self.instructions})

        messages.append({"role": "user", "content": message})

        response = ollama.chat(
            model=self.model,
            messages=messages,
            stream=False
        )

        return response.message.content