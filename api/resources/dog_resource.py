from flask_restful import Resource, reqparse
from api.services.dog_service import DogService

from flask_restful import Resource
from api import api
from flask import make_response, jsonify, request
from ..schemas import dog_schema
from ..models import dog_model
from ..services.dog_service import DogService

class DogResource(Resource):
    def get(self, name=None):
        if name:
            return get_dog_by_name(name)
        return DogService.get_all_dogs()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('breed', required=True)
        parser.add_argument('age', type=int, required=True)
        parser.add_argument('available_for_adoption', type=bool, required=True)
        args = parser.parse_args()

        return DogService.create_dog(args['name'], args['breed'], args['age'], args['available_for_adoption'])

class DogDetails(Resource):
    def get(self, id):
        dog = DogService.get_dog_by_id(id)
        if dog is None:
            return make_response(jsonify("Dog not found."), 400)
        dogschema = dog_schema.DogSchema()
        return make_response(dogschema.jsonify(dog), 200)
    
    def put(self, id):
        dog_bd = DogService.get_dog_by_id(id)
        if dog_bd is None:
            return make_response(jsonify("Dog not found."), 404) # NOT FOUND
        dogschema = dog_schema.DogSchema()
        validate = dogschema.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            json_data = request.get_json()
            new_dog = dog_model.Dog(**json_data)
            update_dog = DogService.update_dog(new_dog, id)
            return make_response(dogschema.jsonify(update_dog), 200)

    def delete(self, id):
        return DogService.delete_dog(id)
    
    
api.add_resource(DogResource, '/dogs')
api.add_resource(DogDetails, '/dogs/<id>')
