from app import db
from app.models.repuesto import Repuesto

def test_create_repuesto(app):
    repuesto = Repuesto(
        nombre="Pastillas de Freno",
        categoria="Frenos",
        marca="Brembo",
        precio=45000.0,
        stock=10,
        descripcion="Pastillas de freno de alto rendimiento"
    )
    db.session.add(repuesto)
    db.session.commit()

    assert repuesto.id is not None
    assert repuesto.nombre == "Pastillas de Freno"
    assert repuesto.categoria == "Frenos"
    assert repuesto.marca == "Brembo"
    assert repuesto.precio == 45000.0
    assert repuesto.stock == 10
    assert repuesto.descripcion == "Pastillas de freno de alto rendimiento"

def test_repuesto_default_stock(app):
    repuesto = Repuesto(
        nombre="Bujía CR8E",
        precio=15000.0
    )
    db.session.add(repuesto)
    db.session.commit()

    assert repuesto.stock == 0  # Valor por defecto

def test_repuesto_repr(sample_repuesto):
    assert repr(sample_repuesto) == "<Repuesto Filtro de Aceite>"
