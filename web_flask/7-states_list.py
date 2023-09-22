#!/usr/bin/python3
''' flask/jinja '''
from flask import Flask, render_template
from markupsafe import escape
from models import storage, state

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def st():
    '''print all states'''
    g = storage.all(state.State)
    return render_template("7-states_list.html", states=g)


@app.teardown_appcontext
def tear_down(response_or_exc):
    '''clean up'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
