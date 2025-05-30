def test_get_courses_success(auth_client):
    response = auth_client.get("/api/courses")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_course_by_code_success(auth_client):
    response = auth_client.get("/api/courses/BSCS")
    assert response.status_code == 200 or response.status_code == 404
