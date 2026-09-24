from app.models import (
    User,
    Moto,
    Cita,
    Repuesto,
    Pedido,
    DetallePedido,
    Factura,
    DetalleFactura,
    Trabajo
)

def test_models_import():
    assert User is not None
    assert Moto is not None
    assert Cita is not None
    assert Repuesto is not None
    assert Pedido is not None
    assert DetallePedido is not None
    assert Factura is not None
    assert DetalleFactura is not None
    assert Trabajo is not None
