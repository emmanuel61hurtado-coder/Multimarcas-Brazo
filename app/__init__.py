from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.security import generate_password_hash
from flask_mail import Mail
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
mail = Mail()


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object('config.Config')

    # 🔌 inicializar extensiones
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    # 🔐 login config
    login_manager.login_view = 'auth.login'
    login_manager.login_message = "Debes iniciar sesión para acceder."
    login_manager.login_message_category = "warning"

    # 👤 loader usuario
    from app.models.user import User
    

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # 📦 BLUEPRINTS
    from app.routes.auth import auth_bp
    from app.routes.home import home_bp
    from app.routes.moto_route import motos_bp
    from app.routes.cita_route import citas_bp
    from app.routes.admin import admin_bp
    from app.routes.repuesto_route import repuestos_bp
    from app.routes.cliente_routes import clientes_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(home_bp)
    app.register_blueprint(clientes_bp,url_prefix='/cliente')
    app.register_blueprint(motos_bp, url_prefix='/motos')
    app.register_blueprint(citas_bp, url_prefix='/citas')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(repuestos_bp, url_prefix='/repuestos')
    from app.routes.carrito_routes import carrito_bp
    app.register_blueprint(carrito_bp, url_prefix='/carrito')

    # 🛠 crear BD + admin por defecto
    with app.app_context():
        import time

        db_url = app.config.get('SQLALCHEMY_DATABASE_URI', '')
        if '@' in str(db_url):
            host_part = str(db_url).split('@')[-1]
            print(f"[INFO] Conectando a la base de datos en: {host_part}")
        else:
            print(f"[INFO] DATABASE_URL configurada: {db_url}")

        max_retries = 5
        for intento in range(1, max_retries + 1):
            try:
                db.create_all()
                print(f"[OK] Conexión a la base de datos exitosa (intento {intento})")
                break
            except Exception as e:
                error_str = str(e)
                if 'could not translate host name' in error_str:
                    print(f"[ERROR] No se puede resolver el host de la base de datos. Verifica que DATABASE_URL apunte a un hostname/IP válido.")
                print(f"[ERROR] Intento {intento}/{max_retries} - {error_str}")
                if intento < max_retries:
                    print(f"[INFO] Reintentando en 3 segundos...")
                    time.sleep(3)
                else:
                    print("[FATAL] No se pudo conectar a la base de datos después de todos los intentos.")
                    raise

        admin = User.query.filter_by(username='admin').first()

        if not admin:
            admin = User(
                nombre_completo='Administrador',
                username='admin',
                email='admin@brazo.com',
                telefono='0000000000',
                rol='admin',
                password=generate_password_hash('admin123'),
                activo=True
            )
            db.session.add(admin)
            db.session.commit()

    return app