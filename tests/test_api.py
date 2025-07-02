# tests/test_api.py
import json
from api.models import Task # Importa tu modelo Task para interactuar con la BD

# Asegúrate de que tus fixtures 'client', 'db' y 'app' se pasen a las funciones de prueba
# cuando necesites interactuar con la base de datos o el contexto de la aplicación.
# La fixture 'session' es la forma preferida de interactuar con la BD en las pruebas.

def test_get_tasks(client, session): # Usamos 'session' para interactuar con la BD
    """
    Prueba el endpoint GET /api/tasks.
    Debe retornar una lista vacía si no hay tareas.
    """
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert json.loads(response.data) == []

def test_create_task(client, session, app): # Usamos 'session' y 'app' para el contexto
    """
    Prueba el endpoint POST /api/tasks.
    Debe crear una nueva tarea y retornarla.
    """
    task_data = {
        "title": "Comprar víveres",
        "description": "Leche, pan, huevos"
    }
    response = client.post('/api/tasks', json=task_data)
    
    assert response.status_code == 201
    response_data = json.loads(response.data)
    assert response_data['title'] == task_data['title']
    assert response_data['description'] == task_data['description']
    assert response_data['done'] == False # Por defecto
    assert 'id' in response_data

    # Verifica que la tarea fue realmente guardada en la base de datos
    with app.app_context(): # Usamos 'app' directamente para el contexto
        # Usamos session.query para asegurar que la consulta se haga en la sesión de prueba
        task_in_db = session.query(Task).filter_by(id=response_data['id']).first()
        assert task_in_db is not None
        assert task_in_db.title == task_data['title']

def test_create_task_missing_title(client, session): # Usamos 'session'
    """
    Prueba el endpoint POST /api/tasks con un título faltante.
    Debe retornar un error 400.
    """
    task_data = {
        "description": "Esta tarea no tiene título"
    }
    response = client.post('/api/tasks', json=task_data)
    assert response.status_code == 400
    # Asumimos que la respuesta de error es JSON. Si no lo es,
    # el json.loads fallará y deberías verificar el contenido HTML (ej. `b"title is required" in response.data`).
    assert "El campo 'title' es obligatorio." in json.loads(response.data)['description']


def test_get_single_task(client, session, app): # Usamos 'session' y 'app' para el contexto
    """
    Prueba el endpoint GET /api/tasks/<id>.
    Debe retornar una tarea específica.
    """
    # Primero, crea una tarea para poder obtenerla
    with app.app_context(): # Usamos 'app' directamente para el contexto
        new_task = Task(title="Leer libro", description="Capítulo 1 de Python")
        session.add(new_task) # Usamos session.add
        session.commit() # Usamos session.commit
        task_id = new_task.id

    response = client.get(f'/api/tasks/{task_id}')
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['id'] == task_id
    assert response_data['title'] == "Leer libro"

def test_get_non_existent_task(client, session): # Usamos 'session'
    """
    Prueba el endpoint GET /api/tasks/<id> para una tarea que no existe.
    Debe retornar un error 404.
    """
    response = client.get('/api/tasks/999') # ID que no existe
    assert response.status_code == 404
    # Asumimos que tu API devuelve JSON para 404. Si no, ajusta la aserción.
    assert "Tarea con ID 999 no encontrada." in json.loads(response.data)['description']

def test_update_task(client, session, app): # Usamos 'session' y 'app' para el contexto
    """
    Prueba el endpoint PUT /api/tasks/<id>.
    Debe actualizar una tarea existente.
    """
    # Crea una tarea para actualizar
    with app.app_context(): # Usamos 'app' directamente para el contexto
        task_to_update = Task(title="Tarea vieja", description="Descripción vieja")
        session.add(task_to_update) # Usamos session.add
        session.commit() # Usamos session.commit
        task_id = task_to_update.id

    updated_data = {
        "title": "Tarea actualizada",
        "description": "Nueva descripción",
        "done": True
    }
    response = client.put(f'/api/tasks/{task_id}', json=updated_data)
    assert response.status_code == 200
    response_data = json.loads(response.data)
    assert response_data['id'] == task_id
    assert response_data['title'] == updated_data['title']
    assert response_data['description'] == updated_data['description']
    assert response_data['done'] == updated_data['done']

    # Verifica que los cambios se reflejaron en la base de datos
    with app.app_context(): # Usamos 'app' directamente para el contexto
        # Usamos session.query para asegurar que la consulta se haga en la sesión de prueba
        task_in_db = session.query(Task).filter_by(id=task_id).first()
        assert task_in_db.title == updated_data['title']
        assert task_in_db.description == updated_data['description']
        assert task_in_db.done == updated_data['done']

def test_update_non_existent_task(client, session): # Usamos 'session'
    """
    Prueba el endpoint PUT /api/tasks/<id> para una tarea que no existe.
    Debe retornar un error 404.
    """
    response = client.put('/api/tasks/999', json={"title": "No existe"})
    assert response.status_code == 404
    # Asumimos que tu API devuelve JSON para 404. Si no, ajusta la aserción.
    assert "Tarea con ID 999 no encontrada." in json.loads(response.data)['description']

def test_delete_task(client, session, app): # Usamos 'session' y 'app' para el contexto
    """
    Prueba el endpoint DELETE /api/tasks/<id>.
    Debe eliminar una tarea existente.
    """
    # Crea una tarea para eliminar
    with app.app_context(): # Usamos 'app' directamente para el contexto
        task_to_delete = Task(title="Tarea a eliminar")
        session.add(task_to_delete) # Usamos session.add
        session.commit() # Usamos session.commit
        task_id = task_to_delete.id

    response = client.delete(f'/api/tasks/{task_id}')
    assert response.status_code == 204 # No Content

    # Verifica que la tarea fue eliminada de la base de datos
    with app.app_context(): # Usamos 'app' directamente para el contexto
        # Usamos session.query para asegurar que la consulta se haga en la sesión de prueba
        task_in_db = session.query(Task).filter_by(id=task_id).first()
        assert task_in_db is None

def test_delete_non_existent_task(client, session): # Usamos 'session'
    """
    Prueba el endpoint DELETE /api/tasks/<id> para una tarea que no existe.
    Debe retornar un error 404.
    """
    response = client.delete('/api/tasks/999') # ID que no existe
    assert response.status_code == 404
    # Asumimos que tu API devuelve JSON para 404. Si no, ajusta la aserción.
    assert "Tarea con ID 999 no encontrada." in json.loads(response.data)['description']
