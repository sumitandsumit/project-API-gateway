from flask import Flask, jsonify, request

app = Flask(__name__)

# Dummy data for demonstration
products = [
    {"id": 1, "name": "Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "price": 150},
]


@app.route("/products", methods=["GET", "POST"])
def manage_products():

    if request.method == "GET":
        response = {"products": products}
        return (jsonify(response), 200)

    elif request.method == "POST":
        # Add a new product
        new_product = request.json
        products.append(new_product)
        return (
            jsonify(
                {"message": "Product added successfully", "new_product": new_product}
            ),
            201,
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
