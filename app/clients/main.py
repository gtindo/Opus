# coding: utf-8
from flask import Flask, jsonify, request

app = Flask(__name__)
app.config['Secret'] = "Secret"

@app.route('/', methods=['GET']) # To prevent Cors issues
def index():
    # Sent in GET requests
    # param = request.args.get('param')
    # Build the response
    response = jsonify({ 'status':'success', 'message': 'Welcome to Opus API.' })
    # Let's allow all Origin requests
    response.headers.add('Access-Control-Allow-Origin', '*') # To prevent Cors issues
    return response

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=7777)