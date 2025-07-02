# api/models.py
from .database import db # Importa la instancia de SQLAlchemy

class Task(db.Model):
    __tablename__ = 'task' # Nombre de la tabla en la base de datos
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(200), nullable=True) # Asegúrate de que esta línea esté presente
    done = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Task {self.id}: {self.title}>'

    # Opcional: un método para serializar el objeto a un diccionario
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done
        }
