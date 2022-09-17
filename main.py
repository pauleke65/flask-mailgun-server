import os

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


@app.route("/send-mail", methods=["POST"])
def getpic():
    req_data = request.get_json()
    name = req_data["name"]
    email = req_data["email"]
    mobile = req_data["mobile"]
    subject = req_data["subject"]
    message = req_data["message"]
    usermail = req_data["usermail"]

    MG_API_KEY = os.getenv("MG_API_KEY")
    MG_HOST = os.getenv("MG_HOST")

    return requests.post(
        f"{MG_HOST}/messages",
        auth=("api", MG_API_KEY),
        data={
            "from": f"{name} <{email}>",
            "to": [email, usermail],
            "subject": subject,
            "html": f"""
            <h4> Email from ${name} ${email} </h4>
            <p> Phone Number: {mobile}
            <p> ${message}</p>
            """,
        },
    )


if __name__ == "__main__":
    app.run(debug=True, port=os.getenv("PORT", default=5000))
