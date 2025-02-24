from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Flaskが動作しています！"

if __name__ == "__main__":
    app.run(debug=True, port=5001)  # ✅ ここでポートを明示的に指定
