def test_index(client):
    response = client.get('/admin/usuarios')
    assert response.status_code == 302
