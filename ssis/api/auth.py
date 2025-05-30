from flask import Blueprint, request, jsonify
from ssis.models.admin import Admin  # adjust path as needed
import jwt
import datetime
from os import getenv

auth = Blueprint('auth_bp', __name__, url_prefix='/api')

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if Admin.validate(username, password):
        payload = {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        token = jwt.encode(payload, getenv("SECRET_KEY"), algorithm="HS256")
        return jsonify({"access_token": token})

    return jsonify({"message": "Invalid credentials"}), 401