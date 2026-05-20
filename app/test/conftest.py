from app import create_app, db
import pytest

@pytest.fixture
def app():
    app = create_app()
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['TESTING'] = True
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def user(app):
    from app.models.user import User
    from werkzeug.security import generate_password_hash
    user = User(
        nombre_completo="test_user",
        username="test_user",
        email="test_user@example.com",
        telefono="1234567890",
        password=generate_password_hash("test_password"),
        rol='cliente',
        activo=True
    )
    db.session.add(user)
    db.session.commit()
    yield user
