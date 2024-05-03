import base64
import binascii
from datetime import datetime, timedelta, timezone

import jwt
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "your_jwt_secret_key"
jwt_manager = JWTManager(app)

# Generate an RSA private key
private_key = rsa.generate_private_key(
    public_exponent=65537, key_size=2048, backend=default_backend()
)

# Serialize the private key to PEM format
pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption(),
)

# Serialize the public key to PEM format
pem_public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo,
)

# Extract the modulus and public exponent from the public key
public_numbers = private_key.public_key().public_numbers()
modulus = public_numbers.n
exponent = public_numbers.e

# Convert the modulus to a byte array (big-endian)
modulus_bytes = modulus.to_bytes((modulus.bit_length() + 7) // 8, byteorder="big")

# Base64URL encode the modulus
modulus_b64 = base64.urlsafe_b64encode(modulus_bytes).decode("utf-8").rstrip("=")

# For simplicity, we'll manually construct a JWK for the public key.
public_jwk = {
    "kty": "RSA",
    "e": base64.urlsafe_b64encode(exponent.to_bytes(3, "big"))
    .decode("utf-8")
    .rstrip("="),
    "n": modulus_b64,
    "alg": "RS256",
    "use": "sig",
}


# @app.route("/auth/login", methods=["POST"])
# def login():
#     if not request.is_json:
#         return jsonify({"msg": "Missing JSON in request"}), 400

#     username = request.json.get("username", None)
#     password = request.json.get("password", None)
#     # For demonstration purpose only
#     if username == "admin" and password == "password":
#         # Create JWT token with the private key
#         access_token = create_access_token(identity=username)
#         return jsonify(access_token=access_token), 200
#     else:
#         return jsonify({"msg": "Bad username or password"}), 401


@app.route("/auth/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username == "admin" and password == "password":
        # 1
        # # Payload with an expiration time
        # payload = {"sub": username, "exp": datetime.utcnow() + timedelta(minutes=30)}
        # # Sign the token with RS256
        # token = jwt.encode(payload, pem_private_key, algorithm="RS256")
        # return jsonify(access_token=token), 200

        # 2
        # #  Create JWT token with the private key
        # # Set the expiration time for the JWT token
        # expires_delta = timedelta(minutes=30)
        # access_token = create_access_token(
        #     identity=username, expires_delta=expires_delta
        # )
        # return jsonify(access_token=access_token), 200

        # 3
        # Manually create the JWT payload
        payload = {
            "sub": username,  # Subject (whom the token refers to)
            "iat": datetime.now(timezone.utc),  # Issued at
            "exp": datetime.now(timezone.utc)
            + timedelta(minutes=30),  # Expiration time
            "iss": "http://localhost:5004",  # Issuer
            "aud": "http://your_audience",  # Audience
        }
        # Sign the JWT with the RSA private key
        access_token = jwt.encode(payload, pem_private_key, algorithm="RS256")
        return jsonify(access_token=access_token), 200

    else:
        return jsonify({"msg": "Bad username or password"}), 401


@app.route("/.well-known/jwks.json", methods=["GET"])
def jwks():
    # Serve the public JWK
    jwks = {"keys": [public_jwk]}
    return jsonify(jwks)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004)
