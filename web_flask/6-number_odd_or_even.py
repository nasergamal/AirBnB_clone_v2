#!/usr/bin/python3
''' flask/jinja '''
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    '''Hello Hbnb!'''
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''Hbnb only'''
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def whatcha_buying(text):
    '''print url content for c'''
    text = text.replace("_", " ")
    return f'C {escape(text)}'


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def whatcha_selling(text="is cool"):
    '''print url content for python'''
    text = text.replace("_", " ")
    return f'Python {escape(text)}'


@app.route("/number/<int:n>", strict_slashes=False)
def numbers_only(n):
    '''int urls only'''
    return f'{n} is a number'


@app.route("/number_template/<int:n>", strict_slashes=False)
def numbers_temp(n):
    '''first jinja template'''
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def numbers_odd(n):
    '''url odd or even'''
    odd = [' is even', ' is odd']

    return render_template("6-number_odd_or_even.html", n=f'{n}{odd[n % 2]}')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
