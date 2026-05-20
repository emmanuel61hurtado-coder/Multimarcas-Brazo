def test_login_success(client, user):
    response = client.post('/auth/login', data={
        'username': 'test_user',
        'password': 'test_password'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_login_invalid_credentials(client):
    response = client.post('/auth/login', data={
        'username': 'wronguser',
        'password': 'wrongpassword'
    }, follow_redirects=True)
    assert response.status_code == 200

def test_login_already_authenticated(client, user):
    from flask_login import login_user
    with client:
        with client.session_transaction() as session:
            session['_user_id'] = str(user.id)
        response = client.get('/auth/login', follow_redirects=True)
        assert response.status_code == 200
