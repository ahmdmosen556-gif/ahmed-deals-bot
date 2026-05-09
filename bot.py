import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# هات التوكن من Environment Variables في Railway
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بيك في بوت أحمد للعروض 🔥\nابعتلي اسم المنتج اللي بتدور عليه")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"بدورلك على: {user_message}...")

def main():
    if not BOT_TOKEN:
        print("Error: BOT_TOKEN not found in environment variables")
        return
    
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()