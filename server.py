from flask import Flask, jsonify

from flask_cors import CORS

app = Flask(__name__)

portOfCall = 8080

@app.route("/api/home", methods = ['GET'])
def return_home():
    return jsonify({
        'message' : 'Hey there, worldy.'
    })

cors = CORS(app)

from server.controllers import user_controller, business_controller

if __name__ == "__main__":
    app.run(debug=True, port = portOfCall)