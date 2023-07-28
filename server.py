from flask_cors import CORS
from flask import Flask, jsonify
from flask import redirect, request, session, flash
from flask_bcrypt import Bcrypt
# from flask_app.controllers import user_controller
# from flask_app.controllers import business_controller
from flask_app.models import user_model, business_model

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)

#### USER
#### USER
#### USER
@app.route('/create_user', methods = ['POST'])
def create_user():
    if request.form['action'] == 'create_user':

        if not user_model.User.validate_user(request.form):
            return redirect('/')

        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        print("HASH BELOW: ")
        print(pw_hash)

        data_row = {
            'first_name' : request.form['first_name'],
            'last_name' : request.form['last_name'],
            'email' : request.form['email'],
            'password' : pw_hash,
            'birthday' : request.form['birthday']
        }

        user_in_db = user_model.User.get_by_email(data_row)
        if user_in_db:
            flash("Sorry, but that email is not available to use.")
            return redirect('/')

        user_id = user_model.User.save(data_row)
        session['user_id'] = user_id
        return redirect('/dashboard')
    

@app.route('/user_login', methods = ['POST'])
def user_login():
    if request.form['action'] == 'user_login':
        data_row = {
            'email' : request.form['email']
        }
        user_in_db = user_model.User.get_by_email(data_row)

        if not user_in_db:
            flash("Invalid Email/Password.")
            return redirect('/')
        if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
            flash("Invalid Email/Password.")
            return redirect('/')

    return redirect('/dashboard')



### BUSINESS
### BUSINESS
### BUSINESS
@app.route('/create_business', methods = ['POST'])
def create_business():
        if not business_model.Business.validate_business(request.form):
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

        business_model.Business.save(data_row)
        return redirect('/dashboard')

@app.route('/edit_business', methods = ['POST'])
def edit_business():
    if not business_model.Business.validate_business(request.form):
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

    business_model.Business.edit_business(data_row)
    return redirect('/dashboard')

@app.route('/delete/<int:id>')
def delete(id):
    business_model.Business.delete({'id' : id})
    return redirect('/dashboard')

if __name__ == "__main__":
    app.run(debug=True, port = 8080)