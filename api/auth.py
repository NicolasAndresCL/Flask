from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask import Blueprint, request, jsonify, abort
from .models import User, db  
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__, url_prefix='/api')


@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'tags': ['Autenticación'],
    'summary': 'Registro de un nuevo usuario',
    'description': 'Crea una cuenta nueva con nombre de usuario y contraseña.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['username', 'password'],
                'properties': {
                    'username': {'type': 'string'},
                    'password': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Usuario creado exitosamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {'type': 'string'}
                }
            }
        },
        400: {
            'description': 'Faltan datos o el usuario ya existe'
        }
    }
})
def register():
    data = request.get_json()
    if not data or not data.get('username') or not data.get('password'):
        abort(400, description="Faltan campos requeridos.")

    if User.query.filter_by(username=data['username']).first():
        abort(400, description="Usuario ya existe.")

    user = User(username=data['username'])
    user.set_password(data['password'])
    db.session.add(user)
    db.session.commit()
    return jsonify(message="Usuario registrado correctamente"), 201

@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Autenticación'],
    'summary': 'Inicio de sesión',
    'description': 'Devuelve un JWT válido si las credenciales son correctas.',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['username', 'password'],
                'properties': {
                    'username': {'type': 'string'},
                    'password': {'type': 'string'}
                }
            }
        }
    ],
    'responses': {
        200: {
            'description': 'Token generado correctamente',
            'schema': {
                'type': 'object',
                'properties': {
                    'access_token': {'type': 'string'}
                }
            }
        },
        401: {
            'description': 'Credenciales inválidas'
        }
    }
})
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    if user and user.check_password(data['password']):
        token = create_access_token(identity=str(user.id))
        return jsonify(access_token=token)
    abort(401, description="Credenciales inválidas.")


