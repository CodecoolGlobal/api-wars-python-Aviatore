# put your code here
from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    url = request.args.get('url', 'https://swapi.dev/api/planets')
    response = requests.get(url)
    obj = response.json()

    return render_template('index.html', data=obj)


@app.route('/planet', methods=['GET'])
def planet():
    url = request.args.get('id')
    obj = None

    if url is not None:
        response = requests.get(url)
        obj = response.json()

    return render_template('planet.html', planet=obj)


if __name__ == '__main__':
    app.run()
