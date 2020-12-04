from src.database import Column, Model, db
from src.todo.models import Todo
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime


class User(Model):
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(80), nullable=False)
    email = Column(db.String(128), unique=True, nullable=False)
    password_hash = Column(db.String(128), nullable=False)
    confirmed = Column(db.Boolean, default=False)
    todos = db.relationship(Todo, backref='user', lazy=True)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def set_password(self, password):
        print('hello')
        if len(password) < 8 or len(password) > 50:
            raise AssertionError('Password must be between 8 and 50 characters')

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.username}>'
