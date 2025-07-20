from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello():
    port = os.getenv("SERVER_PORT", "8081")
    return f"Hello from Python App running on port {port}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("SERVER_PORT", 8081)))

