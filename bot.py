import os
from telegram import Update
from telegram.ext import Application, MessageHandler, ContextTypes, filters

TOKEN =os.getenv("BOT_TOKEN")

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        await update.message.reply_text(
            "မင်္ဂလာပါ 👋\n"
            "Neon Channel မှ ကြိုဆိုပါတယ်။\n"
            "ခဏနေ ပြန်လည်ဆက်သွယ်ပေးပါမယ်။"
        )

app = Application.builder().token(TOKEN).build()

app.add_handler(
    MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply)
)

app.run_polling()
