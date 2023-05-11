from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/ping", methods=["GET"])
def hello_world():
    return jsonify("pong")


@app.route("/vacation-plan", methods=["POST"])
def vacation_plan():
    data = request.get_json()
    return jsonify("Got the data: " + str(data))


if __name__ == "__main__":
    app.run()
