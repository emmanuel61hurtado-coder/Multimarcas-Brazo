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

@pytest.fixture
def admin_user(app):
    from app.models.user import User
    from werkzeug.security import generate_password_hash
    admin = User(
        nombre_completo="Admin User",
        username="admin_user",
        email="admin@example.com",
        telefono="9876543210",
        password=generate_password_hash("admin_password"),
        rol='admin',
        activo=True
    )
    db.session.add(admin)
    db.session.commit()
    yield admin

@pytest.fixture
def empleado_user(app):
    from app.models.user import User
    from werkzeug.security import generate_password_hash
    empleado = User(
        nombre_completo="Empleado User",
        username="empleado_user",
        email="empleado@example.com",
        telefono="5555555555",
        password=generate_password_hash("empleado_password"),
        rol='empleado',
        activo=True
    )
    db.session.add(empleado)
    db.session.commit()
    yield empleado

@pytest.fixture
def sample_moto(app, user):
    from app.models.moto import Moto
    moto = Moto(
        marca="Yamaha",
        modelo="FZ 25",
        placa="XYZ123",
        año=2022,
        color="Negro",
        cilindraje="250cc",
        user_id=user.id
    )
    db.session.add(moto)
    db.session.commit()
    yield moto

@pytest.fixture
def sample_cita(app, user, sample_moto):
    from app.models.cita import Cita
    from datetime import datetime, time
    cita = Cita(
        user_id=user.id,
        moto_id=sample_moto.id,
        fecha=datetime(2026, 10, 1, 10, 0),
        hora=time(10, 0),
        tipo_servicio="Mantenimiento General",
        descripcion="Cambio de aceite y frenos",
        estado="pendiente"
    )
    db.session.add(cita)
    db.session.commit()
    yield cita

@pytest.fixture
def sample_repuesto(app):
    from app.models.repuesto import Repuesto
    repuesto = Repuesto(
        nombre="Filtro de Aceite",
        categoria="Filtros",
        marca="Yamaha",
        precio=25000.0,
        stock=15,
        descripcion="Filtro original para moto Yamaha"
    )
    db.session.add(repuesto)
    db.session.commit()
    yield repuesto

