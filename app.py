from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    real_ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    app.logger.info(f"Visitor IP: {real_ip}")
    return "<h1>Hello!</h1><p>Your visit has been logged.</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
