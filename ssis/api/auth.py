from flask import Blueprint, request, jsonify
from ssis.models.admin import Admin  # adjust path as needed
import jwt
import datetime
from os import getenv

auth = Blueprint('auth_bp', __name__, url_prefix='/api')

@auth.route('/login', methods=['POST'])
def login():
    """
    User login endpoint.
    ---
    tags:
      - Authentication
    parameters:
      - in: body
        name: body
        schema:
          id: Login
          required:
            - username
            - password
          properties:
            username:
              type: string
            password:
              type: string
    responses:
      200:
        description: Successful login
    """
    
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400

    if Admin.validate(username, password):
        payload = {
            "sub": username,  # ✅ This is the subject claim required
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        }
        secret = getenv("SECRET_KEY") or "default-secret"
        token = jwt.encode(payload, secret, algorithm="HS256")

        # Python 3.11+ returns token as bytes, decode to str if needed
        if isinstance(token, bytes):
            token = token.decode('utf-8')

        return jsonify({"access_token": token})

    return jsonify({"message": "Invalid credentials"}), 401
