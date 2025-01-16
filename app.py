from flask import Flask, render_template
from routes import blueprints
from models import initialize_database
import os
from seed import seed

app = Flask(__name__)

# データベースの初期化
initialize_database()

# デモデータを挿入
if "AUTO_SEED" in os.environ and os.environ["AUTO_SEED"] == "True":
    print("Auto seed is enabled.")
    seed(n=200)

# 各Blueprintをアプリケーションに登録
for blueprint in blueprints:
    app.register_blueprint(blueprint)


# ホームページのルート
@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(port=8080, debug=True)
