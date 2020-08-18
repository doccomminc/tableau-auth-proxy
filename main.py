import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def status():
    return "Hello, world!"


@app.route('/', methods=['POST'])
def auth():
    r = requests.post('http://127.0.0.1/trusted',
                      data={'username': 'admin'})
    if r.text == '-1':
        return jsonify({'error': True})
    return jsonify({'error': False,
                    'token': r.text})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
