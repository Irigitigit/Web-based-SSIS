from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from ssis.models.course import Course

courses = Blueprint("courses", __name__, url_prefix="/api/courses")

@courses.route("", methods=["GET"])
@jwt_required()
def get_courses():
    courses_list = Course().course_list()
    return jsonify(courses_list), 200

@courses.route("/<code>", methods=["GET"])
@jwt_required()
def get_course(code):
    courses_list = Course().course_list()
    for course in courses_list:
        if course[0] == code:
            return jsonify(course), 200
    return jsonify({"error": "Course not found"}), 404
