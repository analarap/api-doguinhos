from api import ma
from marshmallow import Schema, fields

class DogSchema(ma.Schema):
    class Meta:
        fields = ('_id', 'name', 'breed', 'age', 'available_for_adoption')
    
    _id = fields.Str()
    name = fields.Str(required=True)
    breed = fields.Str(required=True)
    age = fields.Int(required=True)
    available_for_adoption = fields.Bool(required=True)