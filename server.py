from flask_app import app
from flask import jsonify
from flask_app.models import user_model

@app.route('/api/home', methods = ['GET'])
def call_database():
    # this is where we need to fetch our user data
    userdata = user_model.User.find_all_users()
    print(userdata)
    return jsonify({
        'message' : 'Hello worlds!'
    })

if __name__ == "__main__":
    app.run(debug=True, port = 8080)