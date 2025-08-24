import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# دریافت توکن از متغیر محیطی
TOKEN = os.getenv("TELEGRAM_TOKEN")

# دکمه شیشه‌ای
keyboard = [
    [InlineKeyboardButton("📢 ورود به کانال اصلی", url="https://t.me/traderbotvip")]
]
reply_markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔹برای عضویت در کانال رسمی تریدر بات روی دکمه زیر کلیک کنید:",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("ربات در حال اجراست...")
    app.run_polling()

if __name__ == "__main__":
    main()
