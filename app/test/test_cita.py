from datetime import datetime, time
from app import db
from app.models.cita import Cita

def test_create_cita(app, user, sample_moto):
    fecha_cita = datetime(2026, 11, 15, 9, 30)
    hora_cita = time(9, 30)
    cita = Cita(
        user_id=user.id,
        moto_id=sample_moto.id,
        fecha=fecha_cita,
        hora=hora_cita,
        tipo_servicio="Revisión Tecnomecánica",
        descripcion="Revisión general de la moto"
    )
    db.session.add(cita)
    db.session.commit()

    assert cita.id is not None
    assert cita.user_id == user.id
    assert cita.moto_id == sample_moto.id
    assert cita.fecha == fecha_cita
    assert cita.hora == hora_cita
    assert cita.tipo_servicio == "Revisión Tecnomecánica"
    assert cita.estado == "pendiente"  # Valor por defecto
    assert cita.created_at is not None

def test_cita_repr(sample_cita):
    expected_repr = f"<Cita {sample_cita.fecha} - {sample_cita.estado}>"
    assert repr(sample_cita) == expected_repr

def test_cita_relationships(sample_cita, user, sample_moto):
    assert sample_cita.cliente == user
    assert sample_cita.moto == sample_moto
    assert sample_cita in user.citas
    assert sample_cita in sample_moto.citas
