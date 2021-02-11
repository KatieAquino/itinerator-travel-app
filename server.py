"""Server for Travel App"""

from flask import Flask, jsonify, render_template, request, flash, session, redirect
from model import connect_to_db
import crud
from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = '\xac\x83\x18\xb4\xae\x86\x1c\xefok\xe3\xa5Qrjt\xdd\x83\x95[{\x80'



@app.route('/')
def display_homepage():
    """Show the homepage"""

    return render_template('index.html')


@app.route('/login', methods=['POST'])
def log_in_user():
    """Log in user"""

    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user = crud.find_user_by_email(email)

    if user and user.password == password:
        session['user'] = user.id
        flash('Successfully logged in!')
    
    else:
        flash('Unable to login, please try again')

    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', port='5757', debug=True)