import os
from flask import Flask, jsonify

app = Flask(__name__)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")


@app.route("/")
def home():
    return f"Hello, AWS Cloud Engineer! App version: {APP_VERSION}"


@app.route("/health")
def health():
    return jsonify(status="healthy", version=APP_VERSION)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)

