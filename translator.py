from deep_translator import GoogleTranslator

from helper import AIModel

class Translator:
    def __init__(self, use_ai: bool = False, ai_instructions: str = None):
        self._google_translator = GoogleTranslator(source='auto', target='bn')
        self._ai_translator=None

        if use_ai and ai_instructions:
            self._ai_translator = AIModel(model="qwen2.5:3b", instructions=ai_instructions)

        if use_ai and not ai_instructions:
            print("Warning! Need to provide instructions for AI!")


    def translate(self, message: str):
        primary_translation = self._google_translator.translate(message)

        print(f"Google Translate: {primary_translation}")
        if not self._ai_translator:
            return primary_translation, None
        
        prompt = f"English: {message}, Bengali: {primary_translation}"
        secondary_translation = self._ai_translator.prompt(prompt)

        print(f"AI Assist: {secondary_translation}")
        return primary_translation, secondary_translation