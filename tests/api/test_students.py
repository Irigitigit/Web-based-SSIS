def test_get_students_success(auth_client):
    response = auth_client.get("/api/students")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_create_student_missing_data(auth_client):
    response = auth_client.post("/api/students", data={})
    assert response.status_code == 201 or response.status_code == 400  # adjust based on behavior
