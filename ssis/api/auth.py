from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from ssis.models.admin import Admin

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
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


@auth_bp.route("/user-info", methods=["GET"])
@jwt_required()
def user_info():
    current_user = get_jwt_identity()
    return jsonify({"user": current_user}), 200
