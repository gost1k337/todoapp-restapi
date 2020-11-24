from src.database import Column, Model, db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import validates
from datetime import datetime
import re


class User(Model):
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(80), nullable=False)
    email = Column(db.String(128), unique=True, nullable=False)
    password_hash = Column(db.String(128), nullable=False)
    created_at = Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def set_password(self, password):
        print('-'*30)
        print(password)
        if len(password) < 8 or len(password) > 50:
            raise AssertionError('Password must be between 8 and 50 characters')

        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    @validates('username')
    def validate_username(self, key, username):
        if not username:
            raise AssertionError('No username provided')

        if len(username) < 5 or len(username) > 20:
            raise AssertionError('Username must be between 5 and 20 characters')

        return username

    @validates('email')
    def validate_email(self, key, email):
        if not email:
            raise AssertionError('No email provided')

        if not re.match("[^@]+@[^@]+\.[^@]+", email):
            raise AssertionError('Provided email is not an email address')

        return email

    def save(self):
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return f'<User {self.username}>'
