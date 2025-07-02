from flask import Blueprint, jsonify, request, abort
from .database import db
from .models import Task

api_bp = Blueprint('api', __name__, url_prefix='/api')

def serialize_task(task):
    return {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'done': task.done
    }

@api_bp.route('/tasks', methods=['GET'])
def get_tasks():
    """Obtener todas las tareas"""
    tasks = Task.query.all()
    return jsonify([serialize_task(task) for task in tasks])

@api_bp.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    """Obtener una tarea por su ID"""
    task = db.session.get(Task, task_id)
    if task is None:
        abort(404, description=f"Tarea con ID {task_id} no encontrada.")
    return jsonify(serialize_task(task))

@api_bp.route('/tasks', methods=['POST'])
def create_task():
    """Crear una nueva tarea"""
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
def update_task(task_id):
    """Actualizar una tarea existente"""
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
def delete_task(task_id):
    """Eliminar una tarea existente"""
    task = db.session.get(Task, task_id)
    if task is None:
        abort(404, description=f"Tarea con ID {task_id} no encontrada.")

    db.session.delete(task)
    db.session.commit()
    return '', 204
