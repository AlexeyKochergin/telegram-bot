from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Привет! Это сервер. Telegram-бот работает отдельно."

# Запуск сервера
if __name__ == "__main__":
    app.run(debug=True)
