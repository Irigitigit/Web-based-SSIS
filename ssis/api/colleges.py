from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ssis.models.college import College

colleges_bp = Blueprint("colleges", __name__)

@colleges_bp.route("/colleges", methods=["GET"])
@jwt_required()
def get_colleges():
    colleges = College().college_list()
    return jsonify(colleges), 200

@colleges_bp.route("/colleges/<code>", methods=["GET"])
@jwt_required()
def get_college(code):
    colleges = College().college_list()
    for col in colleges:
        if col[0] == code:
            return jsonify(col), 200
    return jsonify({"error": "College not found"}), 404
