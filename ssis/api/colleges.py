from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ssis.models.college import College

colleges = Blueprint("colleges", __name__, url_prefix="/api/colleges")

@colleges.route("", methods=["GET"])
@jwt_required()
def get_colleges():
    colleges_list = College().college_list()
    return jsonify(colleges_list), 200

@colleges.route("/<code>", methods=["GET"])
@jwt_required()
def get_college(code):
    colleges_list = College().college_list()
    for college in colleges_list:
        if college[0] == code:
            return jsonify(college), 200
    return jsonify({"error": "College not found"}), 404
