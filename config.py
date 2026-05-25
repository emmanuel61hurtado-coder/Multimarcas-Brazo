import os
import secrets

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', secrets.token_urlsafe(24))

    # --- Base de Datos ---
    # Si DATABASE_URL está definida directamente, se usa tal cual.
    # Si no, se construye a partir de las variables individuales (DB_USER, DB_HOST, etc.)
    # Si ninguna existe, se usa SQLite local (para desarrollo).
    @staticmethod
    def _build_database_url():
        # 1. Si ya viene DATABASE_URL completa, usarla
        explicit_url = os.environ.get('DATABASE_URL')
        if explicit_url:
            return explicit_url

        # 2. Construir desde variables individuales
        db_user = os.environ.get('DB_USER')
        db_password = os.environ.get('DB_PASSWORD')
        db_host = os.environ.get('DB_HOST')
        db_port = os.environ.get('DB_PORT', '5432')
        db_name = os.environ.get('DB_NAME')

        if all([db_user, db_password, db_host, db_name]):
            return f"postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

        # 3. Fallback: SQLite local (desarrollo)
        return 'sqlite:///brazo.db'

    SQLALCHEMY_DATABASE_URI = _build_database_url.__func__()
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # --- Correo (Flask-Mail) ---
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', '1', 't']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER', 'noreply@brazo.com')

    # --- Administrador por defecto ---
    ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@brazo.com')
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', 'admin123')

    # --- Seguridad ---
    PASSWORD_RESET_SALT = os.environ.get('PASSWORD_RESET_SALT', 'password-reset-salt')