from flask import Flask, jsonify

from flask_cors import CORS, cross_origin

app = Flask(__name__)

@app.route("/api/home", methods = ['GET'])
def return_home():
    return jsonify({
        'message' : 'Hey there, worldy.'
    })

cors = CORS(app)

# from flask_app.controllers import user_controller
# from flask_app.controllers import business_controller

if __name__ == "__main__":
    app.run(debug=True)