from flask_cors import CORS
from flask import Flask, jsonify
import json
from flask import redirect, request, session, flash
from flask_bcrypt import Bcrypt
# from flask_googlemaps import GoogleMaps, Map
from flask_app.models import user_model, business_model

app = Flask(__name__)
bcrypt = Bcrypt(app)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# app.config['GOOGLEMAPS_KEY'] = "8JZ7i18MjFuM35dJHq70n3Hx4"

# GoogleMaps(app)

# USER
# CREATE
# CREATE
# CREATE

@app.route('/api/create_user', methods=['POST'])# 
def create_user():
    # print("#####################", request.json())
    # x = user_model.User.validate_user(request.data)

    # print(request.data['first_name'])
    # print(request.args.first_name)
    # record = json.loads(request.data)
    print(request.data, '^^^^^')
    for value in request.data:
        print(value, "########")
    return ({'message': 'kitteh'})

    if (not results[0]):
        print("****************************************************I am on line 29!")
        return jsonify(results)

    pw_hash = bcrypt.generate_password_hash(request.form['password'])

    # Add this to the validation function in the user model - Noah
    # user_in_db = user_model.User.get_by_email(data_row)
    # if user_in_db:
    #     flash("Sorry, but that email is not available to use.")
    #     return redirect('/welcome')

    data_row = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password': pw_hash,
        'birthday': request.form['birthday']
    }

    return jsonify((True, user_model.User.save(data_row)))


@app.route('/user_login', methods=['POST'])
def user_login():
    data_row = {
        'email': request.form['email'],
        'password': request.form['password']
    }
    user_in_db = user_model.User.get_by_email(data_row)

    if not user_in_db:
        flash("Invalid Email/Password.")
        return redirect('/welcome')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash("Invalid Email/Password.")
        return redirect('/welcome')

    user_model.User.get_one_user()
    return redirect('/')


# READ
# READ
# READ
@app.route('/one_user')
def one_user():
    user_model.User.get_one_user()
    return redirect('/profile')

# UPDATE
# UPDATE
# UPDATE


@app.route('/user/<int:id>')
def user():
    user_model.User.get_one_user()
    return redirect('/profile')


@app.route('/edit_user', methods=['POST'])
def edit_user():
    user_model.User.edit_user()
    return redirect('/')


# DELETE
# DELETE
# DELETE
@app.route('/delete_user/<int:id>')
def delete_user(id):
    user_model.User.delete({'id': id})
    return redirect('/')

# BUSINESS
# CREATE
# CREATE
# CREATE


@app.route('/create_business', methods=['POST'])
def create_business():
    if not business_model.Business.validate_business(request.form):
        return redirect('/')

    data_row = {
        'type': request.form['type'],
        'name': request.form['name'],
        'address': request.form['address'],
        'phone_number': request.form['phone_number'],
        'business_hours': request.form['business_hours'],
        'offerings': request.form['offerings'],
        'user_id': session['user_id']
    }

    business_model.Business.save(data_row)
    return redirect('/')


# READ
# READ
# READ
@app.route('/one_business/<int:id>')
def get_one_business():
    business_model.Business.get_one_business()


@app.route('/random_business')
def random_business():
    business_model.Business.get_random_business()


@app.route('/get_businesses')
def get_businesses():
    business_model.Business.get_all_businesses_with_user()


# UPDATE
# UPDATE
# UPDATE
@app.route('/edit_business', methods=['POST'])
def edit_business():
    if not business_model.Business.validate_business(request.form):
        business_id = request.form['id']
        flash("Please edit your business again.")
        return redirect(f'/edit_business/{business_id}')

    data_row = {
        'id': request.form['id'],
        'biz': request.form['biz'],
        'name': request.form['name'],
        'address': request.form['address'],
        'phone': request.form['phone'],
        'hours': request.form['hours'],
        'service': request.form['service']
    }

    business_model.Business.edit_business(data_row)
    return redirect('/dashboard')


# DELETE
# DELETE
# DELETE
@app.route('/delete_business/<int:id>')
def delete_business(id):
    business_model.Business.delete({'id': id})
    return redirect('/dashboard')


if __name__ == "__main__":
    app.run(debug=True, port=8080)
