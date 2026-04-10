from flask import Flask
import os

app = Flask(__name__)

SECRET_MSG = os.environ.get("SECRET_MSG", "No secret set")

@app.route("/")
def home():
    return f"<h1>Flask App on Render</h1><p>Secret: {SECRET_MSG}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))