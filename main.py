import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/', methods=['GET'])
def status():
    return jsonify({'success': True})


@app.route('/', methods=['POST'])
def auth():
    try:
        params = request.json
        if params is None:
            return jsonify({'error': True,
                            'message': 'Missing required JSON body',
                            'token': None})

        if 'username' not in params:
            return jsonify({'error': True,
                            'message': 'Missing required JSON parameter `username`',
                            'token': None})
        r = requests.post('http://127.0.0.1/trusted',
                          data={'username': params['username']})
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
