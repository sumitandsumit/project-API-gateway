from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/users", methods=["GET"])
def get_users():
    # Dummy data for demonstration
    users = [
        {"id": 1, "name": "User 1"},
        {"id": 2, "name": "User 2"},
    ]

    response = {"users": users}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
