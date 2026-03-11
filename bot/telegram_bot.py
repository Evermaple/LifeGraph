from telegram.ext import ApplicationBuilder, CommandHandler
from datetime import date
from app.db import get_conn
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")


async def log(update, context):

    mood = int(context.args[0])
    deepwork = float(context.args[1])

    today = date.today().isoformat()

    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
    UPDATE daily_metrics
    SET mood=?, deepwork=?
    WHERE date=?
    """, (mood, deepwork, today))

    conn.commit()

    await update.message.reply_text("saved")


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("log", log))

app.run_polling()
