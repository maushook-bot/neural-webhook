from flask import Flask, request, abort, jsonify

app = Flask(__name__)


@app.route('https://neural-webhook.herokuapp.com/', methods=['POST'])
def webhook():
    headers = request.headers
    bearer = headers.get('Authorization')
    token = bearer.split()[1]

    if request.method == 'POST' and token == 'Perseverance':
        print(request.json, token)
        return jsonify({
            'message': 'Success: Data Received',
            'content': request.json['data'],
        }), 200
    else:
        return jsonify({
            'message': f'Request Failed',
            'content': 'Not Available',
        }), 400



