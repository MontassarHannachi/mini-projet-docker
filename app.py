import os
from flask import Flask

app = Flask(__name__)
MESSAGE = os.environ.get("APP_MESSAGE", "Bonjour depuis le conteneur !")

@app.route("/")
def index():
    return MESSAGE

@app.route("/health")
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
