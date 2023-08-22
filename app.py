import logging
from flask import Flask, request, jsonify
import flask
import requests
import os


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Log flask version
logger.info(f"Flask version: {flask.__version__}")
# Log requests version
logger.info(f"Requests version: {requests.__version__}")

app = Flask(__name__)


@app.route("/test", methods=["GET"])
def test_handler():
    logger.info("Received test request")
    return jsonify({"test": "OK"})


# Translate to telegram
@app.route("/message", methods=["GET"])
def telegram_message():
    logger.info("Received telegram_message request")
    # Read parameters
    message = request.args.get("text")
    # If group parameter is provided
    if request.args.get("group"):
        group = request.args.get("group")
    else:
        group = '-1001655467479'
    # Read token from token.txt
    with open("token.txt", "r") as f:
        token = f.read().strip()    
    # Send message to telegram group via bot
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {
        'chat_id': group,
        'text': message
    }

    response = requests.post(url, json=payload)

    if response.status_code == 200:
        logger.info("Message sent successfully")
        return str(response.status_code), 200
    else:
        logger.error("Failed to send message: " + response.text)
        return str(response.status_code), 400


def main():
    app.run(
        host='0.0.0.0',
        debug=False,
        port=int(os.environ.get("PORT", 2732))
    )


if __name__ == "__main__":
    main()
