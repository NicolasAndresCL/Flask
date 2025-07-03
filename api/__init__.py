# api/__init__.py
from .routes import api_bp
from .auth import auth_bp

def init_api(app):
    if 'api' not in app.blueprints:
        app.register_blueprint(api_bp)
        app.register_blueprint(auth_bp)  # Asegurate de que esta línea exista
