from flask import Flask, request
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def get_client_ip():
    """Return the real client IP, accounting for proxies."""
    # Check common headers used by proxies
    if 'X-Forwarded-For' in request.headers:
        # Sometimes multiple IPs are listed, take the first one
        ip = request.headers['X-Forwarded-For'].split(',')[0].strip()
        return ip
    elif 'X-Real-IP' in request.headers:
        return request.headers['X-Real-IP']
    else:
        # fallback to the remote address
        return request.remote_addr

@app.route("/")
def index():
    client_ip = get_client_ip()
    logging.info(f"Visitor IP: {client_ip} - User-Agent: {request.user_agent.string}")
    return f"Hello! Your IP is {client_ip}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
