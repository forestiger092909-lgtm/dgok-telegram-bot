from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# Главное меню
main_menu = ReplyKeyboardMarkup(
    [['📄 Информация', '📞 Контакты'], ['💡 Совет']],
    resize_keyboard=True
)

# Подменю для "Информация"
info_menu = ReplyKeyboardMarkup(
    [['📊 Отчёты'], ['🔙 Назад']],
    resize_keyboard=True
)

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Привет! Я бот ДГОК-Стандарт. Помогаю с вопросами качества, документацией и стандартами.\n\nВыберите действие:",
        reply_markup=main_menu
    )

# Обработка сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == '📄 Информация':
        await update.message.reply_text("Выберите раздел:", reply_markup=info_menu)

    elif text == '📞 Контакты':
        await update.message.reply_text(
            "📞 Рабочие контакты:\n\n"
            "🔹 ЦСМК:\n"
            "• Шуканов Талгат Лайкович - служебный 42-97 - сотовый - 87023271804 — почта - Talgat.Shukanov@erg.kz\n"
            "• Ибрагимов Рамиль Ризаевич - служебный 49-17 - сотовый - 87051542934 — почта - Ramil.Ibragimov@erg.kz\n\n"
            "🔹 СТАНДАРТИЗАЦИЯ:\n"
            "• Исмаилова Жанар Жарылкасимовна - служебный 48-71 - сотовый - 87058076575 — почта - Zhanar.Ismailova@erg.kz\n"
            "• Рыщанова Камила Муратовна - служебный 49-26 - сотовый - 87078971647 — почта - Kamila.Ryschanova@erg.kz"
        )

    elif text == '💡 Совет':
        await update.message.reply_text("Совет дня: не забывай фиксировать цели — это основа качества 💼")

    elif text == '📊 Отчёты':
        await update.message.reply_text(
            "📋 Отчёты:\n\n"
            "📝 Тестовый отчёт №1:\n"
            "Ф08-ПРЦ — «Отчёт по целям»\n\n"
            "Скоро здесь появятся новые документы!"
        )

    elif text == '🔙 Назад':
        await update.message.reply_text("Вы вернулись в главное меню:", reply_markup=main_menu)

    else:
        await update.message.reply_text("Выберите одну из кнопок ниже.", reply_markup=main_menu)

# Запуск
import os
ApplicationBuilder().token(os.getenv("8309598474:AAGNE8sGiE897FeZ73u6rT37d9I7-OoF5h4")).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

print("Бот запущен и ждёт сообщений...")
app.run_polling()

# redeploy trigger



