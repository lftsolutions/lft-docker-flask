def test_home_access(test_client):
    response = test_client.get('/')
    assert response.status_code == 200
    assert 'home' in response.data.decode('utf-8')