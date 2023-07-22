from flask import app
from flask import render_template, redirect, request, session, flash
from ..models.user_model import User
from ..models.business_model import Business
from flask import Bcrypt
bcrypt = Bcrypt(app)


# Should we include two different html templates here, or have it be the same with 
# rendering dependent on available elements?
# Here, I have one render outcome (welcome.html)
# main page (logged in or logged out) will contain a carusel of pictures/information
# thus the need to include a getAll businesses call here
@app.route('/')
def index(): 
    if "user_id" in session:
        return render_template("welcome.html", businesses = Business.getAll(), 
                            user = User.get_one({"id" : session['user_id']}))
    else:
        return render_template('welcome.html')