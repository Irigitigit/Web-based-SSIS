from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ssis.models.student import Student
from ssis.views.students.utils import save_image

students_bp = Blueprint("students", __name__)

@students_bp.route("/students", methods=["GET"])
@jwt_required()
def list_students():
    students = Student().get_all(paginate=False)
    return jsonify(students), 200

@students_bp.route("/students", methods=["POST"])
@jwt_required()
def create_student():
    data = request.form.to_dict()
    photo_file = request.files.get("photo")
    if photo_file:
        cloud_link = save_image(photo_file)
        data["photo"] = cloud_link

    student = Student(**data)
    student.add_new()
    return jsonify({"message": "Student added successfully"}), 201

@students_bp.route("/students/<id>", methods=["GET"])
@jwt_required()
def get_student(id):
    student = Student().get(id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

@students_bp.route("/students/<id>", methods=["PUT"])
@jwt_required()
def update_student(id):
    data = request.get_json()
    student = Student(id=id, **data)
    student.update()
    return jsonify({"message": "Student updated"}), 200

@students_bp.route("/students/<id>", methods=["DELETE"])
@jwt_required()
def delete_student(id):
    Student.delete(id)
    return jsonify({"message": "Student deleted"}), 200
