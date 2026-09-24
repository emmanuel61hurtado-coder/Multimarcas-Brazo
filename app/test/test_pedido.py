from app import db
from app.models.pedido import Pedido, DetallePedido

def test_create_pedido_web(app, user):
    pedido = Pedido(
        user_id=user.id,
        metodo_entrega="Envío",
        origen="Web",
        direccion_envio="Calle 123 #45-67",
        telefono_contacto="3009876543",
        total=50000.0
    )
    db.session.add(pedido)
    db.session.commit()

    assert pedido.id is not None
    assert pedido.user_id == user.id
    assert pedido.estado == "Pendiente"  # Valor por defecto
    assert pedido.metodo_entrega == "Envío"
    assert pedido.origen == "Web"
    assert pedido.total == 50000.0
    assert pedido.user == user
    assert pedido in user.pedidos

def test_create_pedido_fisico(app, user):
    pedido = Pedido(
        user_id=user.id,
        metodo_entrega="Taller",
        origen="Físico",
        nombre_cliente_fisico="Carlos Gómez",
        total=25000.0
    )
    db.session.add(pedido)
    db.session.commit()

    assert pedido.origen == "Físico"
    assert pedido.nombre_cliente_fisico == "Carlos Gómez"

def test_pedido_repr(app, user):
    pedido = Pedido(
        user_id=user.id,
        metodo_entrega="Taller",
        total=10000.0
    )
    db.session.add(pedido)
    db.session.commit()

    assert repr(pedido) == f"<Pedido {pedido.id} - Pendiente>"

def test_create_detalle_pedido(app, user, sample_repuesto):
    pedido = Pedido(
        user_id=user.id,
        metodo_entrega="Taller",
        total=50000.0
    )
    db.session.add(pedido)
    db.session.commit()

    detalle = DetallePedido(
        pedido_id=pedido.id,
        repuesto_id=sample_repuesto.id,
        cantidad=2,
        precio_unitario=25000.0,
        subtotal=50000.0
    )
    db.session.add(detalle)
    db.session.commit()

    assert detalle.id is not None
    assert detalle.pedido_id == pedido.id
    assert detalle.repuesto_id == sample_repuesto.id
    assert detalle.cantidad == 2
    assert detalle.precio_unitario == 25000.0
    assert detalle.subtotal == 50000.0
    assert detalle.repuesto == sample_repuesto
    assert detalle in pedido.items

def test_detalle_pedido_repr(app, user, sample_repuesto):
    pedido = Pedido(user_id=user.id, metodo_entrega="Taller", total=25000.0)
    db.session.add(pedido)
    db.session.commit()

    detalle = DetallePedido(
        pedido_id=pedido.id,
        repuesto_id=sample_repuesto.id,
        cantidad=1,
        precio_unitario=25000.0,
        subtotal=25000.0
    )
    db.session.add(detalle)
    db.session.commit()

    assert repr(detalle) == f"<DetallePedido {detalle.id} - 1 unidades>"

def test_pedido_cascade_delete(app, user, sample_repuesto):
    pedido = Pedido(user_id=user.id, metodo_entrega="Taller", total=25000.0)
    db.session.add(pedido)
    db.session.commit()

    detalle = DetallePedido(
        pedido_id=pedido.id,
        repuesto_id=sample_repuesto.id,
        cantidad=1,
        precio_unitario=25000.0,
        subtotal=25000.0
    )
    db.session.add(detalle)
    db.session.commit()

    detalle_id = detalle.id
    db.session.delete(pedido)
    db.session.commit()

    assert DetallePedido.query.get(detalle_id) is None
