from flask_jwt_extended import create_access_token, get_jwt_identity
from src.database import db
from flask import jsonify
from src.auth.models import User
from src.auth.schemas import user_schema, users_schema, UserSchema, user_in_schema

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = 'HS256'


class AuthService(object):
    def login(self, request):
        email, password = request.json.get('email'), request.json.get('password')
        errors = user_in_schema.validate({'email': email, 'password': password})
        if errors:
            return jsonify({'message': errors})
        is_exist = self.is_user_exist(email)
        if not is_exist:
            return jsonify({'message': 'User doesn\'t exist'}), 400

        access_token = create_access_token(identity=email)

        return jsonify(access_token=access_token), 200

    def register(self, request):
        username, email, password = request.json.get('username'), request.json.get('email'),\
                                    request.json.get('password')
        is_exist = self.is_user_exist(email)
        if is_exist:
            return jsonify({'message': 'User with this email already exists'}), 400
        user = User(email=email, password_hash=password, username=username)
        access_token = create_access_token(identity=user.id)
        user.save()
        return jsonify(access_token=access_token), 200

    def is_user_exist(self, email):
        return db.session.query(db.exists().where(User.email == email)).scalar()
