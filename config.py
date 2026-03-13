import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TOKEN")
AI_INSTRUCTIONS = os.getenv("AI_INSTRUCTIONS")
AI_ASSIST = os.getenv("AI_ASSIST", "False").lower() == "true"
