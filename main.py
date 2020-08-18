import requests
from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET'])
def status():
    return jsonify({'success': True})


@app.route('/', methods=['POST'])
def auth():
    try:
        r = requests.post('http://127.0.0.1/trusted',
                          data={'username': 'admin'})
    except Exception as e:
        return jsonify({'error': True,
                        'message': str(e),
                        'token': None})
    if r.text == '-1':
        return jsonify({'error': True,
                        'token': None})
    return jsonify({'error': False,
                    'token': r.text})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9987, debug=True)
