#!/usr/bin/python3
''' flask/jinja
'''

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''hello Hbnb'''
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Hbnb only'''
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def whatcha_buying(text):
    '''print url content'''
    text = text.replace("_", " ")
    return f'C {escape(text)}'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
