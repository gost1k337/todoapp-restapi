from marshmallow import fields, Schema
from src.extensions import ma, db
from datetime import datetime
from .models import User


class UserSchema(Schema):
    id = fields.Integer(required=False, dump_only=True)
    username = fields.Str()
    email = fields.Email(error_messages={'null': 'Email is required'})
    password = fields.Str(load_only=True, error_messages={'null': 'Password is required.'})
    created_at = fields.DateTime(default=datetime.utcnow, required=False, dump_only=True)

    class Meta:
        fields = ('id', 'username', 'password', 'email', 'created_at')
        sqla_session = db.session


user_schema = UserSchema()
user_in_schema = UserSchema()
users_schema = UserSchema(many=True)
