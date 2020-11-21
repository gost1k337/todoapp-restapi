from src.database import Column, Model, db
from datetime import datetime


class User(Model):
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(80), nullable=False)
    email = Column(db.String(128), unique=True, nullable=False)
    password_hash = Column(db.String(128), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}>'
