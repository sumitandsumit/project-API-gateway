from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/orders", methods=["GET"])
def get_orders():
    # Dummy data for demonstration
    orders = [
        {"id": 1, "name": "Order 1", "pricePaid": 100, "orderedBy": "user 1"},
        {"id": 2, "name": "Order 2", "pricePaid": 150, "orderedBy": "user 2"},
    ]

    response = {"orders": orders}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
