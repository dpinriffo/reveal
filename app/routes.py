from app import app
from flask import render_template, request, jsonify
import requests
import os


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/add_message', methods=['POST'])
def add_message():
    message = request.form['message']
    message1 = request.form['message1']
    message2 = request.form['message2']
    return render_template('message.html', message=message)


@app.route("/forward", methods=['POST'])
def forward():
    message = request.form['message']
    message1 = request.form['message1']
    message2 = request.form['message2']

    os.environ['HTTPS_PROXY'] = 'https://UShR2cd2LwvS3HhTauX5MnaK:808288fa-cde1-47ee-aff3-1f2a2cbd968f@tntj04mooeq.SANDBOX.verygoodproxy.com:8080'
    res = requests.post('https://echo.apps.verygood.systems/post',
                        json={'card-expiration-date': message,
                            'card-number': message1,
                            'card-security-number': message2}, verify='cert.pem')

    res = res.json()
    return render_template('forward.html', response=res)
