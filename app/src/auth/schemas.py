from marshmallow import fields, Schema
from src.extensions import db
from datetime import datetime


class UserSchema(Schema):
    id = fields.Integer(required=False, dump_only=True)
    username = fields.Str()
    email = fields.Email(error_messages={'null': 'Email is required'})
    password = fields.Str(load_only=True, error_messages={'null': 'Password is required.'})
    confirmed = fields.Boolean(required=False)
    created_at = fields.DateTime(default=datetime.utcnow, required=False, dump_only=True)

    class Meta:
        fields = ('id', 'username', 'password', 'email', 'boolean', 'created_at')
        sqla_session = db.session


user_schema = UserSchema()
user_in_schema = UserSchema()
users_schema = UserSchema(many=True)
