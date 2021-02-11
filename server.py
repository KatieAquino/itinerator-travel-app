"""Server for Travel App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
from jinja2 import StrictUndefined


app = Flask(__name__)


@app.route('/')
def display_homepage():
    """Show the homepage"""

    return render_template('index.html')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port='5757', debug=True)