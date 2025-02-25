import os
from flask import Flask, render_template

print(dir())  # 現在のスクリプトで使える変数や関数を一覧表示
print(__name__)

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

app = Flask(__name__, 
            template_folder=os.path.join(BASE_DIR, "html"), 
            static_folder=os.path.join(BASE_DIR, "static"))

@app.route("/")
def home():
    return render_template("index.html", title="動的なデザイン", message="PythonでWebデザイン！")  # `my_project/html/index.html` を探す
    

if __name__ == "__main__":
    app.run(debug=True)
    print("flask_test")