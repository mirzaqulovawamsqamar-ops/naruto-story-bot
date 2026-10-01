#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Telegram bot for Naruto Story Bot"""

import os
import logging
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
from anthropic import Anthropic

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

if not ANTHROPIC_API_KEY:
    raise RuntimeError("ANTHROPIC_API_KEY topilmadi. .env faylida kiriting.")
if not TELEGRAM_BOT_TOKEN:
    raise RuntimeError("TELEGRAM_BOT_TOKEN topilmadi. .env faylida kiriting.")

client = Anthropic(api_key=ANTHROPIC_API_KEY)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🔥 Naruto Hikoya Botga xush kelibsiz!\n\n"
        "Mavzu yozing, men sizga Naruto olamida hikoya yozaman.\n"
        "Masalan: 'Naruto va Sasuke final battle'"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    prompt = update.message.text.strip()
    if not prompt:
        await update.message.reply_text("Mavzu yozing.")
        return

    await update.message.reply_text("⏳ Hikoya yozilmoqda...")

    system_prompt = """
    Siz Naruto universe asosida professional hikoya yozuvchi sifatida ishlaysiz.
    Hikoya professional, epik, qiziqarli va o'zbek tilida bo'lsin.
    Naruto, Sasuke, Sakura, Kakashi, Itachi, Pain, Madara, Orochimaru, Hinata, Gaara, Shikamaru va boshqa qahramonlar Naruto olamiga mos ravishda ishtirok etsin.
    Janglar, sirlar, qahramon rivojlanishi va drama bo'lsin.
    """

    try:
        response = client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=2500,
            system=system_prompt,
            messages=[{"role": "user", "content": prompt}],
        )
        text = response.content[0].text
        chunks = [text[i:i + 4000] for i in range(0, len(text), 4000)]
        for chunk in chunks:
            await update.message.reply_text(chunk)
    except Exception as exc:
        logger.exception("Error generating story")
        await update.message.reply_text(f"Xato yuz berdi: {exc}")


def main() -> None:
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Telegram bot ishga tushdi")
    app.run_polling()


if __name__ == "__main__":
    main()
