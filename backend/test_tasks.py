import pytest
from app import create_app
from extensions import db
from models import Task

@pytest.fixture
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

def test_valid_transition(app):
    with app.app_context():
        task = Task(title="Test")
        db.session.add(task)
        db.session.commit()

        assert task.can_transition("IN_PROGRESS") == True

def test_invalid_transition(app):
    with app.app_context():
        task = Task(title="Test", status="DONE")
        db.session.add(task)
        db.session.commit()

        assert task.can_transition("TODO") == False