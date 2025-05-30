from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from ssis.models.admin import Admin

auth = Blueprint("auth", __name__, url_prefix="/api")

@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password are required"}), 400

    if Admin.validate(username, password):
        token = create_access_token(identity=username)
        return jsonify({"access_token": token}), 200

    return jsonify({"error": "Invalid credentials"}), 401

