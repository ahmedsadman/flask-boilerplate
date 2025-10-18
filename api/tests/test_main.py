def test_healthcheck(client):
    response = client.get('/ping')
    assert response.status_code == 200
