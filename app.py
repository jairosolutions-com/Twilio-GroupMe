from flask import Flask, jsonify
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    if request.method == 'GET':
        data = {"data": "Hello World"}
        return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)