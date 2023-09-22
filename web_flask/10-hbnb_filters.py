#!/usr/bin/python3
''' flask/jinja '''

from flask import Flask, render_template
from markupsafe import escape
from models import storage, state, amenity

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states_and_state():
    '''fill up filters with db'''
    s = storage.all(state.State)
    a = storage.all(amenity.Amenity)
    return render_template("10-hbnb_filters.html", states=s, amenities=a)


@app.teardown_appcontext
def tear_down(response_or_exc):
    '''cleanup'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
