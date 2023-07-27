from flask_app import app
from flask import render_template, redirect, request, session, flash, jsonify
from flask_app.models import user_model
from flask_app.models import business_model
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/')
def index():
    if "user_id" in session:
        return render_template("page.jsx", businesses = business_model.Business.getAll(), 
            user = user_model.User.get_one({"_id" : session['user_id']}))
    return render_template('page.jsx')

@app.route('/dashboard')
def dashboard():
    if "user_id" in session:
        return render_template("page.jsx", user = user_model.User.get_one({"_id" : session['user_id']}))
    return render_template('page.jsx')

@app.route('/welcome')
def login():
    return render_template('page.jsx')

@app.route('/register', methods = ['post'])
def user_register():
    if request.form['action'] == 'register':

            # User model validation can be utilized here; improper 
            # validation creates redirect to login page (above)
            if not user_model.User.validate_user(request.form):
                return redirect('/welcome')

            pw_hash = bcrypt.generate_password_hash(request.form['password'])

            print(f"NEW USER PW HASH IS {pw_hash}")

            data_row = {
                'first_name' : request.form['first_name'],
                'last_name' : request.form['last_name'],
                'email' : request.form['email'],
                'password' : pw_hash,
                'birthday' : request.form['birthday']
            }


            user_in_db = user_model.User.get_by_email(data_row)
            if user_in_db:
                flash("That email has already been taken. Try using another email.")
                return redirect('/welcome')
            # IF
            # if email is not in database, proceed with User model function to 
            # save entry, save session, and proceed to Map page
            # variable can be created (below) to keep session usable
            user_model.User.register_user(data_row)
            # attempting to create usable session AFTER user is completely registered
            # previous way is below

            user_id = user_model.User.get_by_email(data_row.email)
            session['user_id'] = user_id
            return redirect('/dashboard')
    
    elif request.form['action'] == 'login':
        data_row = {
            'email' : request.form['email']
        }
        user_in_db = user_model.User.get_by_email(data_row)

        if not user_in_db:
            flash("Unknown email. Are you sure you have that right?")
            return redirect('/welcome')
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            flash("Your passwords don't match up. Try again, if it really is you.")
            return redirect('/welcome')

        session['user_id'] = user_in_db._id
        return redirect('/dashboard')