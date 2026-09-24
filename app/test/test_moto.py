import pytest
from app import db
from app.models.moto import Moto
from sqlalchemy.exc import IntegrityError

def test_create_moto(app, user):
    moto = Moto(
        marca="Honda",
        modelo="CB 190R",
        placa="ABC999",
        año=2021,
        color="Rojo",
        cilindraje="190cc",
        user_id=user.id
    )
    db.session.add(moto)
    db.session.commit()

    assert moto.id is not None
    assert moto.marca == "Honda"
    assert moto.modelo == "CB 190R"
    assert moto.placa == "ABC999"
    assert moto.año == 2021
    assert moto.color == "Rojo"
    assert moto.cilindraje == "190cc"
    assert moto.user_id == user.id

def test_moto_repr(sample_moto):
    assert repr(sample_moto) == "<Moto Yamaha FZ 25 - XYZ123>"

def test_moto_propietario_relationship(sample_moto, user):
    assert sample_moto.propietario == user
    assert sample_moto in user.motos

def test_moto_unique_placa(app, user, sample_moto):
    duplicate_moto = Moto(
        marca="Suzuki",
        modelo="GIXER",
        placa="XYZ123",  # Placa duplicada
        user_id=user.id
    )
    db.session.add(duplicate_moto)
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()
