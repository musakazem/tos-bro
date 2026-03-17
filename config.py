import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
AI_INSTRUCTIONS = os.getenv("AI_INSTRUCTIONS")
AI_ASSIST = os.getenv("AI_ASSIST", "False").lower() == "true"

OPENROUTER_TOKEN = os.getenv("OPENROUTER_TOKEN")
OPENROUTER_BASE_URL = os.getenv("OPENROUTER_BASE_URL")
OPENROUTER_MODEL = os.getenv("OPENROUTER_MODEL")