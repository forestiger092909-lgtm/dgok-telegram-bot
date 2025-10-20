import ssl
import certifi
import httpx

# Обход ошибки SSL-сертификата
httpx._config.DEFAULT_CA_BUNDLE_PATH = certifi.where()
ssl._create_default_https_context = ssl._create_unverified_context

from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Меню кнопок
main_menu = ReplyKeyboardMarkup(
    [['📄 Информация', '📞 Контакты'], ['💡 Советы']],
    resize_keyboard=True
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет, Ram! 👋 Я твой бот.\nВыбери действие ниже:",
        reply_markup=main_menu
    )

# Обработка выбора кнопок
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '📄 Информация':
        await update.message.reply_text("Вот информация, которую ты искал...")
    elif text == '📞 Контакты':
        await update.message.reply_text("Наши контакты: +7 777 123 4567")
    elif text == '💡 Советы':
        await update.message.reply_text("Совет дня: не забывай пить воду 💧")
    else:
        await update.message.reply_text("Выбери одну из кнопок ниже.")

# Запуск бота
app = ApplicationBuilder().token("8309598474:AAHNpHhN8s3nVphRPnmSQLA0H6oDhI8uPGQ").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен и ждёт сообщений...")
app.run_polling()
