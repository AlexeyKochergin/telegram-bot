from flask import Flask, request, jsonify
import base64

app = Flask(__name__)

@app.route('/copy', methods=['POST'])
def copy():
    data = request.json
    token = data.get("token")

    # Логика обработки запроса с токеном
    # Здесь можно добавить свою логику, например, проверку токена и генерировать JS-код

    if token == "7582343855:AAEMJG9pvCg335jVCJt0PeDkgI9L38Xj7WE":  # Проверка токена
        # Пример скрипта, который будет выполнен на клиенте
        output = """
        (function() {
            console.log("Скрипт успешно загружен и выполнен!");
            // Тут могут быть любые другие действия
        })();
        """
        encoded_output = base64.b64encode(output.encode('utf-8')).decode('utf-8')
        return jsonify({"output": encoded_output})
    else:
        return jsonify({"error": "Invalid token"}), 400

if __name__ == '__main__':
    app.run(debug=True)
