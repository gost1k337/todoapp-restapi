from marshmallow import fields
from flask_marshmallow import Schema
from .models import User


class UserSchema(Schema):
    id = fields.Integer()
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    created_at = fields.DateTime()

    class Meta:
        fields = ('id', 'email', 'username', 'created_at')


user_schema = UserSchema()
