# api/models.py
from .database import db # Importa la instancia de SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


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

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
