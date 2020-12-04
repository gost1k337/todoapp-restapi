from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash
from src.database import db
from flask import jsonify
from src.auth.models import User
from src.auth.schemas import user_schema, users_schema, user_in_schema

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = 'HS256'


class AuthService(object):
    def login(self, email, password):

        is_exist = self.is_user_exist(email)
        if not is_exist:
            return jsonify({'message': {'email': 'User doesn\'t exist'}}), 400

        user = User.query.filter_by(email=email).first()
        if not user.check_password(password):
            return jsonify({'message': {'password': 'Password is not correct'}})

        access_token = create_access_token(identity=email)

        return jsonify(access_token=access_token), 200

    def register(self, email, password, username):
        is_exist = self.is_user_exist(email)
        if is_exist:
            return jsonify({'message': {'email': 'User with this email already exists'}}), 400
        password_hash = generate_password_hash(password)
        user = User(email=email, password_hash=password_hash, username=username)
        access_token = create_access_token(identity=user.id)
        user.save()
        return jsonify(access_token=access_token), 200

    def is_user_exist(self, email):
        return db.session.query(db.exists().where(User.email == email)).scalar()
