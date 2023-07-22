from flask import app
from flask import render_template, redirect, request, session, flash
from ..models.user_model import User

from flask import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def resgister():
    return render_template('register.html')