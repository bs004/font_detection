# -*- coding: utf-8 -*-

# Importing required libraries

from flask import Flask, request, jsonify
from engine import Predict
import os
import ujson
import requests
from PIL import Image
from io import BytesIO



# Defining configuration
Predict=Predict()

# for flask app

app = Flask(__name__)

# Initial route

@app.route('/', methods = ['GET','POST'])
def index():
    return('Hello from the Other Side !')

# Handler for HTTP POST to http://myhost.com/predict

@app.route('/predict', methods = ['GET','POST'])

def on_incoming_message():

    if request.method == 'POST':
        image_url = request.json['url']

        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))

        final_json=Predict.find_label(image)

        return ujson.dumps(final_json)
    else :
        return jsonify({'status': 'Not Okay'}), 404


if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")