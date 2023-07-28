from flask_app import app
from flask import render_template, redirect, request, session, flash
from models.user_model import User
from models.business_model import Business

from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/new_business')
def new_sighting():
    if "user_id" in session:
        return render_template("new_business.html", user = User.get_one({"id":session['user_id']}))
    else:
        return redirect('/')
    
@app.route('/create_business', methods = ['post'])
def create_business():
        if not Business.validate_business(request.form):
            return redirect('/new_business')

        data_row = {
            'type' : request.form['type'],
            'name' : request.form['name'],
            'address' : request.form['address'],
            'phone_number' : request.form['phone_number'],
            'business_hours' : request.form['business_hours'],
            'offerings' : request.form['offerings'],
            'user_id' : session['user_id']
        }

        return redirect('/dashboard')
    
@app.route('/show_business/<int:id>')
def show_business(id):
    if "user_id" in session:
        return render_template("show_business.html", Business = Business.get_business_with_user({"id" : id}), 
                            user = User.get_one({"id" : session['user_id']}))
    else:
        return redirect('/')

@app.route('/edit_business/<int:id>')
def edit_business(id):
    if 'user_id' in session:
        return render_template("edit_business.html", business = Business.get_business({"id" : id}), 
                            user = User.get_one({"id": session['user_id']}))
    else:
        return redirect('/')

@app.route('/edit_business', methods = ['post'])
def edit_business():
    if 'user_id' not in session:
        return redirect('/')
    if not Business.validate_business(request.form):
        business_id = request.form['id']
        flash("Please edit your business again.")
        return redirect(f'/edit_business/{business_id}')

    data_row = {
        'id' : request.form['id'],
        'type' : request.form['type'],
        'name' : request.form['name'],
        'address' : request.form['address'],
        'phone_number' : request.form['phone_number'],
        'business_hours' : request.form['business_hours'],
        'offerings' : request.form['offerings']
    }

    Business.edit_business(data_row)
    return redirect('/dashboard')


@app.route('/delete/<int:id>')
def delete(id):
    Business.delete({'id' : id})
    return redirect('/dashboard')

# @app.route('/like_business', methods = ['POST'])
# def like_business():
#     Business.like_business({'id' : id})
#     return redirect