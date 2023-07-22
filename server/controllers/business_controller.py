from flask import app
from flask import render_template, redirect, request, session, flash
from ..models.user_model import User
from ..models.business_model import Business

# Should we include two different html templates here, or have it be the same with rendering dependent on available elements?
# Here, I have two different html render outcomes (business_loggedin.html and business_loggedout.html)
@app.route('/business_view/<int:id>')
def view_business(id):
    if "user_id" in session: 
        return render_template('business_loggedin.html', business = Business.getOneLoggedIn({"id" : id}), user = User.get_one({"id" : session['user_id']}))
    else:
        return render_template('business_loggedout.html', business = Business.getOneLoggedOut({"id" : id}))