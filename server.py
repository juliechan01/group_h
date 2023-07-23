from flask import Flask, jsonify
from flask_cors import CORS
# from server.controllers import user_controller, business_controller, home_controller

app = Flask(__name__)
cors = CORS(app)


# **** fetch route for frontend will be 127.0.0.1:8080/api/home
@app.route("/api/home", methods = ['GET'])
def return_home():
    return jsonify({
        # placeholder for now
        'message' : 'Annyeong, world.'
    })

if __name__ == "__main__":
    # we can remove debug=true when app is ready for production
    app.run(debug=True, port = 8080)