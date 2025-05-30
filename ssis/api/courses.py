from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ssis.models.course import Course

courses_bp = Blueprint("courses", __name__)

@courses_bp.route("/courses", methods=["GET"])
@jwt_required()
def get_courses():
    courses = Course().course_list()
    return jsonify(courses), 200

@courses_bp.route("/courses/<code>", methods=["GET"])
@jwt_required()
def get_course(code):
    courses = Course().course_list()
    for course in courses:
        if course[0] == code:
            return jsonify(course), 200
    return jsonify({"error": "Course not found"}), 404
