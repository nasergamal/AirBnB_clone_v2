#!/usr/bin/python3
''' flask/jinja '''
from flask import Flask, render_template
from markupsafe import escape
from models import storage, state

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def states_and_cities():
    '''print all states and cities within'''
    g = storage.all(state.State)
    return render_template("8-cities_by_states.html", states=g)


@app.teardown_appcontext
def tear_down(response_or_exc):
    '''clean up'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
