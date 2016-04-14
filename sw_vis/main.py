import flask
import json
from flask import render_template

from utils import get_vehicle_speeds

app = flask.Flask(__name__)

@app.route('/')
def home():
    vehicle_speeds = get_vehicle_speeds()
    return render_template('home.html', vehicle_speeds=json.dumps(vehicle_speeds))

def start_server():
    app.run(debug=True)