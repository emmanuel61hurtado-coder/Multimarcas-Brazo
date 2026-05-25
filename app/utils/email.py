from itsdangerous import URLSafeTimedSerializer
from flask_mail import Message
from flask import current_app, render_template, url_for
from app import mail

def get_reset_token(user_id, expires_sec=1800):
    """Genera un token seguro que expira en 30 minutos (1800 seg)"""
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    return s.dumps({'user_id': user_id}, salt='password-reset-salt')

def verify_reset_token(token, expires_sec=1800):
    """Verifica el token y devuelve el ID del usuario si es válido"""
    s = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
    try:
        data = s.loads(token, salt='password-reset-salt', max_age=expires_sec)
        return data['user_id']
    except Exception:
        return None


