from marshmallow import Schema, fields
from datetime import datetime


class TodoSchema(Schema):
    id = fields.Integer()
    title = fields.Str()
    completed = fields.Boolean()
    user_id = fields.Integer()
    created_at = fields.DateTime(default=datetime.utcnow, required=False, dump_only=True)

    class Meta:
        fields = ('id', 'title', 'completed', 'created_at')


todo_schema = TodoSchema()
users_schema = TodoSchema(many=True)
