# tests/conftest.py
import pytest
from app import create_app
from api.database import db as global_db

@pytest.fixture(scope='function')
def app():
    app = create_app(testing=True)
    yield app
    with app.app_context():
        global_db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def db(app):
    with app.app_context():
        global_db.create_all()
        yield global_db
        global_db.drop_all()

@pytest.fixture(scope='function')
def session(db, app):
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()
        db.session.bind = connection
        yield db.session
        transaction.rollback()
        connection.close()
        db.session.remove()
