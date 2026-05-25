from app import create_app, db
from app.models.repuesto import Repuesto
from app.utils.repuestos_seed_data import repuestos_data

def run_seed():
    app = create_app()
    with app.app_context():
        agregados = 0
        for nombre, cat, marca, precio, stock, desc in repuestos_data:
            existe = Repuesto.query.filter_by(nombre=nombre).first()
            if not existe:
                nuevo = Repuesto(
                    nombre=nombre,
                    categoria=cat,
                    marca=marca,
                    precio=precio,
                    stock=stock,
                    descripcion=desc
                )
                db.session.add(nuevo)
                agregados += 1

        db.session.commit()
        print(f"[OK] Se agregaron {agregados} repuestos nuevos.")
        print(f"Total en inventario: {Repuesto.query.count()} repuestos.")

if __name__ == '__main__':
    run_seed()
