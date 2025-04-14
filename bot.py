from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Токен для бота (замени на свой токен)
TOKEN = '7582343855:AAEMJG9pvCg335jVCJt0PeDkgI9L38Xj7WE'  # Здесь должен быть твой токен

# Команда /start для бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Пришли мне ссылку на сайт, я создам для тебя скрипт.")

# Обработчик для получения ссылок и генерации скриптов
async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    if not url.startswith("http"):
        await update.message.reply_text("Это не ссылка. Пришли мне ссылку на сайт.")
        return

    await update.message.reply_text("Генерирую скрипт...")

    script = f"""
(function() {{
    const token = "{TOKEN}";  // Токен для работы с Telegram API
    // Генерация скрипта для Tilda
    alert("Скрипт для вставки в консоль.");
}})();
    """

    await update.message.reply_text(f"Вот скрипт для вставки в консоль:\n\n{script}")

# Настройка и запуск бота
def main():
    app_telegram = Application.builder().token(TOKEN).build()  # Убедись, что токен передается правильно
    app_telegram.add_handler(CommandHandler("start", start))  # Добавляем обработчик команды /start
    app_telegram.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))  # Обработка других сообщений
    app_telegram.run_polling()  # Запуск бота

# Запуск бота
if __name__ == "__main__":
    main()
