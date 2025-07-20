import os
from flask import Flask

app = Flask(__name__)
port = int(os.getenv("SERVER_PORT", 8080))  # default 8080 if not found

@app.route("/")
def home():
    return "Hello from Python!"

if __name__ == "__main__":
    print(f"Starting app on port {port}")
    app.run(host="0.0.0.0", port=port)
