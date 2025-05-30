from ssis.models import cursor
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from ssis.models.student import Student
from ssis.views.students.utils import save_image

students = Blueprint("students", __name__, url_prefix="/api/students")

@students.route("", methods=["GET"])
@jwt_required()
def list_students():
    students_list = Student().get_all(paginate=False)
    return jsonify(students_list), 200

@students.route("", methods=["POST"])
@jwt_required()
def create_student():
    """
    Create a new student record
    ---
    tags:
      - Students
    consumes:
      - multipart/form-data
      - application/json
    parameters:
      - name: id
        in: formData
        type: string
        required: true
      - name: firstName
        in: formData
        type: string
        required: true
      - name: middleName
        in: formData
        type: string
      - name: lastName
        in: formData
        type: string
        required: true
      - name: gender
        in: formData
        type: string
        required: true
      - name: yearLevel
        in: formData
        type: integer
        required: true
      - name: course
        in: formData
        type: string
        required: true
      - name: college
        in: formData
        type: string
        required: true
      - name: photo
        in: formData
        type: file
        required: false
    responses:
      201:
        description: Student added successfully
      400:
        description: Missing or invalid fields
      401:
        description: Unauthorized (JWT required)
    """
    
    if request.content_type.startswith("application/json"):
        data = request.get_json()
        photo_file = None  # No file in JSON request
    elif request.content_type.startswith("multipart/form-data"):
        data = request.form.to_dict()
        photo_file = request.files.get("photo")
    else:
        return jsonify({"error": "Unsupported Content-Type"}), 400

    # Validate required fields
    required_fields = ['id', 'firstName', 'lastName', 'yearLevel', 'gender', 'course', 'college']
    for field in required_fields:
        if not data.get(field):
            return jsonify({"error": f"{field} is required"}), 400

    # Convert yearLevel to int safely
    try:
        data['yearLevel'] = int(data['yearLevel'])
    except (ValueError, TypeError):
        return jsonify({"error": "yearLevel must be an integer"}), 400

    # Save photo if provided
    if photo_file:
        data["photo"] = save_image(photo_file)
    else:
        data["photo"] = None

    student = Student(**data)
    student.add_new()
    return jsonify({"message": "Student added successfully"}), 201


@students.route("/<id>", methods=["GET"])
@jwt_required()
def get_student(id):
    student = Student.get_student(id)
    if student:
        return jsonify(student), 200
    return jsonify({"error": "Student not found"}), 404

@students.route("/<id>", methods=["PUT"])
@jwt_required()
def update_student(id):
    data = request.get_json()

    # Validation and type conversion
    if "yearLevel" in data:
        try:
            data["yearLevel"] = int(data["yearLevel"])
        except (ValueError, TypeError):
            return jsonify({"error": "yearLevel must be an integer"}), 400

    # Force id from URL param
    data["id"] = id

    student = Student(**data)
    student.update()
    return jsonify({"message": "Student updated"}), 200

@students.route("/<id>", methods=["DELETE"])
@jwt_required()
def delete_student(id):
    Student.delete(id)
    return jsonify({"message": "Student deleted"}), 200

# ssis/api/students.py

def get(self, student_id: str) -> dict:
    query = "SELECT * FROM students WHERE student_id = %s"
    cursor.execute(query, (student_id,))
    result = cursor.fetchone()
    if result:
        return {
            "student_id": result[0],
            "name": result[1],
            "email": result[2],
            "course_code": result[3]
        }
    return None

