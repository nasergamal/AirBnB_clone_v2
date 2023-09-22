#!/usr/bin/python3
''' flask web app
    two routes
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''hello Hbnb'''
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Hbnb only'''
    return 'HBNB'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
