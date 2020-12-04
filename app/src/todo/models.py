from src.database import Column, Model, db
from datetime import datetime


class Todo(Model):
    id = Column(db.Integer, primary_key=True)
    title = Column(db.String(255), nullable=False)
    completed = Column(db.Boolean, default=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.title}>'
