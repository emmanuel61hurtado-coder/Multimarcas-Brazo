import pytest
from app import db
from app.models.factura import Factura, DetalleFactura
from sqlalchemy.exc import IntegrityError

def test_create_factura(app, user):
    factura = Factura(
        numero="FAC-001",
        user_id=user.id,
        subtotal=100000.0,
        iva=19000.0,
        total=119000.0,
        metodo_pago="Efectivo"
    )
    db.session.add(factura)
    db.session.commit()

    assert factura.id is not None
    assert factura.numero == "FAC-001"
    assert factura.user_id == user.id
    assert factura.visible_cliente is True  # Valor por defecto
    assert factura.subtotal == 100000.0
    assert factura.iva == 19000.0
    assert factura.total == 119000.0
    assert factura.metodo_pago == "Efectivo"

def test_factura_relationships(app, user, empleado_user, sample_moto, sample_cita):
    factura = Factura(
        numero="FAC-002",
        user_id=user.id,
        empleado_id=empleado_user.id,
        moto_id=sample_moto.id,
        cita_id=sample_cita.id,
        subtotal=50000.0,
        iva=9500.0,
        total=59500.0,
        metodo_pago="Transferencia",
        calificacion=5,
        comentario_cliente="Excelente servicio"
    )
    db.session.add(factura)
    db.session.commit()

    assert factura.user == user
    assert factura.empleado == empleado_user
    assert factura.moto == sample_moto
    assert factura.cita == sample_cita
    assert factura in user.facturas
    assert factura in empleado_user.facturas_asignadas
    assert factura in sample_moto.facturas
    assert sample_cita.factura_rel == [factura] or factura in sample_cita.factura_rel

def test_factura_unique_numero(app, user):
    factura1 = Factura(numero="FAC-100", user_id=user.id)
    db.session.add(factura1)
    db.session.commit()

    factura2 = Factura(numero="FAC-100", user_id=user.id)
    db.session.add(factura2)
    with pytest.raises(IntegrityError):
        db.session.commit()
    db.session.rollback()

def test_create_detalle_factura(app, user):
    factura = Factura(numero="FAC-003", user_id=user.id, subtotal=30000.0, total=30000.0)
    db.session.add(factura)
    db.session.commit()

    detalle = DetalleFactura(
        factura_id=factura.id,
        descripcion="Cambio de aceite",
        cantidad=1,
        precio_unitario=30000.0,
        subtotal=30000.0
    )
    db.session.add(detalle)
    db.session.commit()

    assert detalle.id is not None
    assert detalle.factura_id == factura.id
    assert detalle.descripcion == "Cambio de aceite"
    assert detalle.cantidad == 1
    assert detalle.precio_unitario == 30000.0
    assert detalle.subtotal == 30000.0
    assert detalle.factura == factura
    assert detalle in factura.items

def test_factura_cascade_delete(app, user):
    factura = Factura(numero="FAC-004", user_id=user.id)
    db.session.add(factura)
    db.session.commit()

    detalle = DetalleFactura(
        factura_id=factura.id,
        descripcion="Alineación",
        cantidad=1,
        precio_unitario=20000.0,
        subtotal=20000.0
    )
    db.session.add(detalle)
    db.session.commit()

    detalle_id = detalle.id
    db.session.delete(factura)
    db.session.commit()

    assert db.session.get(DetalleFactura, detalle_id) is None
