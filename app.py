# app.py
from flask import Flask, render_template, render_template_string, request, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flasgger import Swagger
from werkzeug.exceptions import HTTPException
import json

from api.database import db
from api import init_api

def create_app(testing=False):
    app = Flask(__name__)
    CORS(app)

    # Configuración adaptable para desarrollo/pruebas
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:' if testing else 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = testing

    db.init_app(app)
    init_api(app)  # Registra el Blueprint una sola vez

    # Swagger
    app.config['SWAGGER'] = {
        'title': 'Mi API de Tareas',
        'uiversion': 3,
        'specs_route': '/apidocs/',
        'specs': [
            {
                'endpoint': 'apidocs_spec',
                'route': '/apidocs_spec.json',
                'rule_filter': lambda rule: True,
                'model_filter': lambda tag: True,
                }
        ]
    }
    Swagger(app)

    # Error handlers
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        response = e.get_response()
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response

    @app.errorhandler(Exception)
    def handle_general_exception(e):
        return jsonify({
            "code": 500,
            "name": "Internal Server Error",
            "description": str(e),
        }), 500

    # Rutas HTML simples
    @app.route('/')
    def home():
        return render_template("index.html")

    @app.route('/about')
    def about():
        return render_template("about.html")

    if testing:
        with app.app_context():
            db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
