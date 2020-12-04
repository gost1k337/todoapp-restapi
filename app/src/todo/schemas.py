from marshmallow import Schema, fields
from datetime import datetime


class TodoSchema(Schema):
    id = fields.Integer(required=False, dump_only=True)
    title = fields.Str()
    completed = fields.Boolean(required=False)
    user_id = fields.Integer(required=False, dump_only=True)
    created_at = fields.DateTime(default=datetime.utcnow, required=False, dump_only=True)

    class Meta:
        fields = ('id', 'title', 'completed', 'created_at')


todo_schema = TodoSchema()
todos_schema = TodoSchema(many=True)
