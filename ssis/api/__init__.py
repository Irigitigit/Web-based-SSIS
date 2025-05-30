from flask import Blueprint, jsonify

# Import each sub-blueprint
from .auth import auth_bp
from .students import students_bp
from .colleges import colleges_bp
from .courses import courses_bp

# Create a parent Blueprint
api = Blueprint("api", __name__, url_prefix="/api")

# Register all sub-blueprints to the main API blueprint
api.register_blueprint(auth_bp)
api.register_blueprint(students_bp)
api.register_blueprint(colleges_bp)
api.register_blueprint(courses_bp)

@api.route("/ping", methods=["GET"])
def ping():
    return jsonify({"message": "API is working!"}), 200