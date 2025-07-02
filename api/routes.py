from flask import Blueprint, jsonify, request, abort
from .database import db
from .models import Task
from flasgger import swag_from


api_bp = Blueprint('api', __name__, url_prefix='/api')

def serialize_task(task):
    return {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'done': task.done
    }

@api_bp.route('/tasks', methods=['GET'])
@swag_from({
    'tags': ['Tareas'],
    'summary': 'Obtener todas las tareas',
    'responses': {
        200: {
            'description': 'Lista de tareas',
            'schema': {
                'type': 'array',
                'items': {
                    'type': 'object',
                    'properties': {
                        'id': {'type': 'integer'},
                        'title': {'type': 'string'},
                        'description': {'type': 'string'},
                        'done': {'type': 'boolean'}
                    }
                }
            }
        }
    }
})
def get_tasks():
    tasks = Task.query.all()
    return jsonify([serialize_task(task) for task in tasks])

@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
@swag_from({
    'tags': ['Tareas'],
    'summary': 'Obtener una tarea por ID',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la tarea a obtener'
        }
    ],
    'responses': {
        200: {
            'description': 'Tarea encontrada',
            'schema': {
                'type': 'object',
                'properties': {
                    'id': {'type': 'integer'},
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'done': {'type': 'boolean'}
                }
            }
        },
        404: {
            'description': 'Tarea no encontrada'
        }
    }
})
def get_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        abort(404, description=f"Tarea con ID {task_id} no encontrada.")
    return jsonify(serialize_task(task))

@api_bp.route('/tasks', methods=['POST'])
@swag_from({
    'tags': ['Tareas'],
    'summary': 'Crear una nueva tarea',
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'required': ['title'],
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'done': {'type': 'boolean'}
                }
            }
        }
    ],
    'responses': {
        201: {
            'description': 'Tarea creada correctamente'
        },
        400: {
            'description': 'Solicitud inválida'
        }
    }
})
def create_task():
    data = request.get_json()
    if not data or 'title' not in data:
        abort(400, description="El campo 'title' es obligatorio.")
    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        done=data.get('done', False)
    )
    db.session.add(new_task)
    db.session.commit()
    return jsonify(serialize_task(new_task)), 201



@api_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@swag_from({
    'tags': ['Tareas'],
    'summary': 'Actualizar una tarea existente',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la tarea a actualizar'
        },
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'title': {'type': 'string'},
                    'description': {'type': 'string'},
                    'done': {'type': 'boolean'}
                }
            }
        }
    ],
    'responses': {
        200: {'description': 'Tarea actualizada'},
        400: {'description': 'Solicitud inválida'},
        404: {'description': 'Tarea no encontrada'}
    }
})
def update_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        abort(404, description=f"Tarea con ID {task_id} no encontrada.")
    data = request.get_json()
    if not data:
        abort(400, description="Se requiere un cuerpo de solicitud JSON.")
    task.title = data.get('title', task.title)
    task.description = data.get('description', task.description)
    task.done = data.get('done', task.done)
    db.session.commit()
    return jsonify(serialize_task(task))

@api_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@swag_from({
    'tags': ['Tareas'],
    'summary': 'Eliminar una tarea existente',
    'parameters': [
        {
            'name': 'task_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID de la tarea a eliminar'
        }
    ],
    'responses': {
        204: {'description': 'Tarea eliminada correctamente'},
        404: {'description': 'Tarea no encontrada'}
    }
})
def delete_task(task_id):
    task = db.session.get(Task, task_id)
    if task is None:
        abort(404, description=f"Tarea con ID {task_id} no encontrada.")
    db.session.delete(task)
    db.session.commit()
    return '', 204
