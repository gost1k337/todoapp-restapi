from flask import Blueprint, jsonify, request
from src.services.auth import AuthService
from sqlalchemy.orm import Query
from .models import User

auth = AuthService()

URL_RESOURCE = '/api/auth'

blueprint = Blueprint('auth', __name__)


@blueprint.route(f'{URL_RESOURCE}/login', methods=('POST',))
def login_user():
    email = request.json.get('email')
    user = User.query.filter_by(email=email).first()
    print(user)
    return jsonify({'email': email})


@blueprint.route(f'{URL_RESOURCE}/register', methods=('POST',))
def register_user():
    return jsonify({'username': 'register'})

