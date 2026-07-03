import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging to see activity in your Railway deployment logs
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Fetch the token from Railway's Environment Variables
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Responds to anyone who starts the bot."""
    user = update.effective_user
    logger.info(f"User {user.first_name} ({user.id}) started the bot.")
    
    # Your custom welcome message
    welcome_text = (
        f"Hello {user.first_name}!\n\n"
        "📈 **FinanceGrowthBot** helps you learn personal finance, "
        "improve money habits, and grow long-term wealth with simple, practical tips."
    )
    
    # Inline button linking to your Telegram channel
    keyboard = [
        [
            InlineKeyboardButton("Join Finance Masters Channel 🚀", url="https://t.me/financemasters1")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Send message with the button attached
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup, parse_mode="Markdown")

def main() -> None:
    """Start the bot using polling (ideal for Background Workers)."""
    if not TOKEN:
        logger.error("No TELEGRAM_BOT_TOKEN found in environment variables!")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Run the bot continuously
    logger.info("Bot is starting up...")
    application.run_polling()

if __name__ == "__main__":
    main()
