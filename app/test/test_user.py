import pytest
from app import db
from app.models.user import User
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError

def test_create_user(app):
    user = User(
        nombre_completo="Juan Perez",
        username="juanp",
        email="juan@example.com",
        telefono="3001234567",
        password=generate_password_hash("password123")
    )
    db.session.add(user)
    db.session.commit()

    assert user.id is not None
    assert user.nombre_completo == "Juan Perez"
    assert user.username == "juanp"
    assert user.email == "juan@example.com"
    assert user.rol == "cliente"  # Valor por defecto
    assert user.activo is True    # Valor por defecto

def test_is_admin(user, admin_user, empleado_user):
    assert user.is_admin() is False
    assert empleado_user.is_admin() is False
    assert admin_user.is_admin() is True

def test_is_empleado(user, admin_user, empleado_user):
    assert user.is_empleado() is False
    assert admin_user.is_empleado() is True
    assert empleado_user.is_empleado() is True

def test_user_repr(user):
    assert repr(user) == "<User test_user>"

def test_user_unique_username(app, user):
    duplicate_user = User(
        nombre_completo="Otro Usuario",
        username="test_user",  # Username duplicado
        email="otro@example.com",
        password="password123"
    )
    db.session.add(duplicate_user)
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()

def test_user_unique_email(app, user):
    duplicate_user = User(
        nombre_completo="Otro Usuario",
        username="otro_user",
        email="test_user@example.com",  # Email duplicado
        password="password123"
    )
    db.session.add(duplicate_user)
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()
