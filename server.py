from flask import Flask, jsonify
from flask_cors import CORS
from server.controllers import user_controller, business_controller

app = Flask(__name__)
portOfCall = 8080
cors = CORS(app)

@app.route("/api/home", methods = ['GET'])
def return_home():
    return jsonify({
        'message' : 'Hey there, worldy.'
    })

if __name__ == "__main__":
    app.run(debug=True, port = portOfCall)