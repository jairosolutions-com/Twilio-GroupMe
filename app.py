import requests, json

from flask import Flask, abort, request, jsonify
from requests.structures import CaseInsensitiveDict

BOT_ID = "8c44cf8a3d72faa3e74fe2fb28"

app = Flask(__name__)

@app.route('/')
def index():
    """
    This function handles the root route and returns a simple "Hello World!" message.
    """
    return "Hello World! -- from index()"


@app.route('/send', methods=['POST'])
def send():
    """
    This function handles the '/send' route and returns a simple "Hello World!" message.
    """
    return "Hello World! -- from send()"

@app.route('/webhook', methods=['POST'])
def webhook():
    """
    This function handles the '/webhook' route and processes incoming webhook requests.
    It extracts the message and phone number from the request and calls the 'send_message' function.
    """
    if request.method == 'POST':
        msg = request.values.get('Body', '').lower()
        phone_num = request.values.get('From','')
        send_message(msg, phone_num)
        return '', 200 
    else:
        abort(400)
		
def send_message(msg,num):
    """
    This function sends a message to the GroupMe API using the provided message and phone number.
    It constructs the API request payload and sends a POST request to the API endpoint.
    """
    url = "https://api.groupme.com/v3/bots/post"
    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"

    data_dict = {
        "bot_id"  : BOT_ID,
        "text"    : f"Number: {num} Message: {msg}"
    }

    data = json.dumps(data_dict)
    resp = requests.post(url, headers=headers, data=data)

    print(resp.status_code)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)