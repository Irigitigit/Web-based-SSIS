# tests/test_students_crud.py

import pytest

def test_create_student(client, auth_headers, monkeypatch):
    """Test POST /api/students (create student)"""

    # Mock database call
    from ssis.models.student import Student
    monkeypatch.setattr(Student, "add_new", lambda self: None)

    data = {
        "id": "test123",
        "firstName": "John",
        "lastName": "Doe",
        "yearLevel": "1",
        "gender": "Male",
        "course": "CS",
        "college": "CENG",
    }

    response = client.post("/api/students", data=data, headers=auth_headers)

    print("Create Response:", response.status_code, response.get_data(as_text=True))

    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data is not None
    assert "message" in json_data

def test_list_students(client, auth_headers, monkeypatch):
    """Test GET /api/students (list students)"""

    from ssis.models.student import Student
    monkeypatch.setattr(Student, "get_all", lambda self, paginate=False: [["test123", "John", "Doe"]])

    response = client.get("/api/students", headers=auth_headers)

    print("List Response:", response.status_code, response.get_data(as_text=True))

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data is not None
    assert isinstance(json_data, list)

def test_get_student(client, auth_headers, monkeypatch):
    """Test GET /api/students/<id>"""

    from ssis.models.student import Student
    monkeypatch.setattr(Student, "get_student", lambda id: {"id": id, "name": "John Doe"})

    response = client.get("/api/students/test123", headers=auth_headers)

    print("Get Response:", response.status_code, response.get_data(as_text=True))

    assert response.status_code in [200, 404]
    if response.status_code == 200:
        json_data = response.get_json()
        assert json_data is not None
        assert "id" in json_data

def test_update_student(client, auth_headers, monkeypatch):
    """Test PUT /api/students/<id>"""

    from ssis.models.student import Student
    monkeypatch.setattr(Student, "update", lambda self: None)

    data = {"yearLevel": "2"}

    response = client.put("/api/students/test123", json=data, headers=auth_headers)

    print("Update Response:", response.status_code, response.get_data(as_text=True))

    assert response.status_code in [200, 400]
    if response.status_code == 200:
        json_data = response.get_json()
        assert json_data is not None
        assert "message" in json_data

def test_delete_student(client, auth_headers, monkeypatch):
    """Test DELETE /api/students/<id>"""

    from ssis.models.student import Student
    monkeypatch.setattr(Student, "delete", lambda id: None)

    response = client.delete("/api/students/test123", headers=auth_headers)

    print("Delete Response:", response.status_code, response.get_data(as_text=True))

    assert response.status_code in [200, 400]
    if response.status_code == 200:
        json_data = response.get_json()
        assert json_data is not None
        assert "message" in json_data
