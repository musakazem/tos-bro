import logging
import re

from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from deep_translator import GoogleTranslator

TOKEN = ""

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def strip_emojis(text: str) -> str:
    return re.sub(r'[^\w\s\d\-_\.,!?;:\'"()\[\]{}@#$%&*+=<>/\\|~`^]', '', text, flags=re.UNICODE).strip()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello! I'll translate English messages to Bengali!")

async def translate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.info(f"Full update: {update}")
    logger.info(f"Message text: {update.message.text}")
    logger.info(f"Message caption: {update.message.caption}")
    logger.info(f"Forward origin: {update.message.forward_origin}")

    if not update.message or not update.message.text:
        return

    text = update.message.text
    chat_type = update.message.chat.type
    user = update.message.from_user.username or update.message.from_user.first_name

    clean_text = strip_emojis(text)
    if not clean_text:
        logger.warning("Message was empty after stripping emojis")
        return

    # Log every incoming message
    logger.info(f"[{chat_type}] {user}: {clean_text}")

    try:
        translated = GoogleTranslator(source='auto', target='bn').translate(clean_text)

        if update.message.forward_origin:
            label = "🌐 (forwarded)"
        else:
            label = "🌐"

        await update.message.reply_text(f"{label} {translated}")
    except Exception as e:
        logger.error(f"Translation failed: {str(e)}")

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    start_handler = CommandHandler('start', start)
    # Removed ChatType filter — works in private chats AND groups now
    translate_handler = MessageHandler(
        filters.TEXT & (~filters.COMMAND),
        translate
    )

    application.add_handler(start_handler)
    application.add_handler(translate_handler)

    print("Bot is running...")
    application.run_polling()