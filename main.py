import os
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welkom bij Vantage IB Support 👋\n\n"
        "Typ:\n"
        "- ib\n"
        "- mt5\n"
        "- spread\n"
        "- support"
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (update.message.text or "").lower()

    if "ib" in text:
        await update.message.reply_text(
            "✅ IB aanmelden:\n"
            "Stuur je naam + e-mail + land.\n"
            "Dan help ik je direct verder."
        )
    elif "mt5" in text:
        await update.message.reply_text(
            "📈 MT5 hulp:\n"
            "• Login probleem\n"
            "• Geen quotes\n"
            "• Cannot trade\n"
            "Stuur een screenshot + uitleg."
        )
    elif "spread" in text:
        await update.message.reply_text(
            "💰 Spread & commissie:\n"
            "Afhankelijk van accounttype (STP/ECN).\n"
            "Zeg welk instrument (bv XAUUSD)."
        )
    elif "support" in text:
        await update.message.reply_text(
            "👤 Support:\n"
            "Stel je vraag hier in de groep, ik reageer."
        )
    else:
        await update.message.reply_text(
            "Ik luister 👂 Typ: ib / mt5 / spread / support"
        )

def main():
    if not BOT_TOKEN:
        raise RuntimeError("BOT_TOKEN ontbreekt")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot draait...")
    app.run_polling()

if __name__ == "__main__":
    main()
