def test_get_colleges_success(auth_client):
    response = auth_client.get("/api/colleges")
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)

def test_get_college_by_code_success(auth_client):
    response = auth_client.get("/api/colleges/CITCS")
    assert response.status_code == 200 or response.status_code == 404
