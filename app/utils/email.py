from itsdangerous import URLSafeTimedSerializer
from flask import current_app

def get_reset_token(user_id, expires_sec=1800):
    """Genera un token seguro que expira en 30 minutos (1800 seg)"""
    salt_val = current_app.config.get('PASSWORD_RESET_SALT', 'password-reset-salt')
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return s.dumps({'user_id': user_id}, salt=salt_val)

def verify_reset_token(token, expires_sec=1800):
    """Verifica el token y devuelve el ID del usuario si es válido"""
    salt_val = current_app.config.get('PASSWORD_RESET_SALT', 'password-reset-salt')
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token, salt=salt_val, max_age=expires_sec)
        return data['user_id']
    except Exception:
        return None


