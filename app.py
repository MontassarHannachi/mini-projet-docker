
from flask import Flask
import os

app = Flask(__name__)

MESSAGE = os.getenv(
    "WELCOME_MESSAGE",
    "Bienvenue dans mon application Docker !"
)

@app.route("/")
def home():
    return MESSAGE

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
