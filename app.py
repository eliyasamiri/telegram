import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# دریافت مقادیر از متغیرهای محیطی (در Railway تنظیم می‌کنیم)
TOKEN = os.environ["TELEGRAM_TOKEN"]                 # توکن ربات
PORT = int(os.environ.get("PORT", "8080"))           # پورت که Railway تعیین می‌کند
WEBHOOK_BASE = os.environ.get("WEBHOOK_BASE", "")    # مثلا: https://your-app.up.railway.app

# دکمه شیشه‌ای
keyboard = [[InlineKeyboardButton("📢 ورود به کانال اصلی", url="https://t.me/traderbotvip")]]
reply_markup = InlineKeyboardMarkup(keyboard)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔹برای عضویت در کانال رسمی تریدر بات روی دکمه زیر کلیک کنید:",
        reply_markup=reply_markup
    )

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))

    # اگر WEBHOOK_BASE تنظیم شده باشد، با webhook اجرا می‌کنیم؛ وگرنه polling
    if WEBHOOK_BASE:
        # URL نهایی وبهوک، مثل: https://your-app.up.railway.app/webhook
        webhook_url = WEBHOOK_BASE.rstrip("/") + "/webhook"
        print(f"Starting webhook at: {webhook_url}")
        app.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            webhook_url=webhook_url
        )
    else:
        print("WEBHOOK_BASE not set -> falling back to polling.")
        app.run_polling()

if __name__ == "__main__":
    main()
