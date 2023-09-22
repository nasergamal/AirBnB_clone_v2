#!/usr/bin/python3
''' flask/jinja '''
from flask import Flask, render_template
from markupsafe import escape
from models import storage, state

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_and_state(id=None):
    '''print all states or selected state and cities within'''
    g = storage.all(state.State)
    if id:
        for v in g.values():
            if v.id == id:
                return render_template("9-states.html", state=v)
        return render_template("9-states.html")
    return render_template("9-states.html", states=g)


@app.teardown_appcontext
def tear_down(response_or_exc):
    '''clean up'''
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
