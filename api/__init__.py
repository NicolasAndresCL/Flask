# api/__init__.py
from .routes import api_bp

def init_api(app):
    if 'api' not in app.blueprints:
        app.register_blueprint(api_bp)
