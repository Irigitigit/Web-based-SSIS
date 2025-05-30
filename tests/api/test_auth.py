def test_login_success(client):
    response = client.post('/api/login', json={
        "username": "miko",
        "password": "pogiako123"
    })
    assert response.status_code == 200
    assert "access_token" in response.get_json()

def test_login_failure(client):
    response = client.post('/api/login', json={
        "username": "wrong",
        "password": "wrong"
    })
    assert response.status_code == 401
