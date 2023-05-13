from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request

import openai

app = Flask(__name__)
app.config.from_object(__name__)


CORS(app, resources={r"/*": {"origins": "*"}})

API_KEY = "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"
openai.api_key = API_KEY


@app.route("/ping", methods=["GET"])
def hello_world():
    return jsonify("pong")


@app.route("/vacation-plan", methods=["POST"])
def vacation_plan():
    data = request.get_json()
    current_location = data["current_location"]
    destination = data["destination"]
    duration = data["duration"]
    budget = data["budget"]

    return generate_vacation_plan(current_location, destination, duration, budget)


def generate_vacation_plan(current_location, destination, duration, budget):
    # content = f"Assume the role of an expert travel advisor. Give an intensive detailed vacation for an customer who wants to travel from {current_location} to {destination} for {duration} days. The budget for the vacation is {budget} chinese yuan. Give a plan in chinese"
    system_content = "You are an expert travel advisor"
    user_content = f"Give an intensive detailed vacation for an customer who wants to travel from {current_location} to {destination} for {duration} days. The budget for the vacation is {budget} chinese yuan. Give a plan in chinese including\n 1. Top tourist attractions.\n 2. Best restaurants in {destination} (according to the budget).\n 3. Best tours.\n 4. Best hotels in {destination} (according to the budget).\n 5. Top things to avoid.\n 6. Top outdoor activities.\n"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_content},
            {"role": "user", "content": user_content},
        ],
    )
    return response.get("choices")[0].get("message").get("content")


if __name__ == "__main__":
    app.run()
