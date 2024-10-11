from api import ma
from marshmallow import Schema, fields

class DogSchema(Schema):
    name = fields.Str(required=True)
    breed = fields.Str(required=True)
    age = fields.Int(required=True)
    available_for_adoption = fields.Bool(required=True)