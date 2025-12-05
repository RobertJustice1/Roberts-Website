from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    # Render passes the real client IP through this header
    real_ip = request.headers.get("X-Forwarded-For")
    
    # If the header is missing, fallback (still 127.0.0.1 on Render)
    if real_ip:
        real_ip = real_ip.split(",")[0].strip()
    else:
        real_ip = request.remote_addr

    app.logger.info(f"Visitor IP: {real_ip}")

    return f"<h1>Hello!</h1><p>Your IP: {real_ip}</p>"
