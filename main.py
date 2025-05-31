from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = '7225067372:AAHJwGF6DE6E4dq9jNkX6Tq7b6ObRQG4BcM'

# Хэштеги, которые отслеживаем
TRACKED_HASHTAGS = ['#босвин', '#спортик', '#злоба']
hashtag_counts = {tag: 0 for tag in TRACKED_HASHTAGS}

async def handle_message(update, context: ContextTypes.DEFAULT_TYPE):
    global hashtag_counts
    if update.message and update.message.text:
        text = update.message.text.lower()
        response = ""

        for tag in TRACKED_HASHTAGS:
            if tag in text:
                hashtag_counts[tag] += 1
                response += f'Найден {tag}! Всего: {hashtag_counts[tag]}\n хуй яйца яйца сосать член'

        if response:
            await update.message.reply_text(response.strip())

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))

print("Бот запущен. Нажми Ctrl+C для выхода.")
app.run_polling()
