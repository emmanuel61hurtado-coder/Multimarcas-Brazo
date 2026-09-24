from app import db
from app.models.trabajo import Trabajo

def test_create_trabajo(app):
    trabajo = Trabajo(
        descripcion="Reparación de motor y sincronización",
        mecanico="Pedro Mecánico",
        repuestos="Empacadura de culata, Bujía",
        costo=150000.0
    )
    db.session.add(trabajo)
    db.session.commit()

    assert trabajo.id is not None
    assert trabajo.descripcion == "Reparación de motor y sincronización"
    assert trabajo.mecanico == "Pedro Mecánico"
    assert trabajo.repuestos == "Empacadura de culata, Bujía"
    assert trabajo.costo == 150000.0

def test_trabajo_cita_relationship(app, sample_cita):
    trabajo = Trabajo(
        descripcion="Mantenimiento preventivo",
        mecanico="Mario Bros",
        costo=80000.0,
        cita_id=sample_cita.id
    )
    db.session.add(trabajo)
    db.session.commit()

    assert trabajo.cita_id == sample_cita.id
