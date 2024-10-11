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
        return get_all_dogs()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('breed', required=True)
        parser.add_argument('age', type=int, required=True)
        parser.add_argument('available_for_adoption', type=bool, required=True)
        args = parser.parse_args()

        return create_dog(args['name'], args['breed'], args['age'], args['available_for_adoption'])

class DogDetails(Resource):
    def get(self, id):
        dog = DogService.get_dog_by_name(name)
        if dog is None:
            return make_response(jsonify("Doguinho não encontrado."), 400)
        dogschema = dog_schema.DogSchema()
        return make_response(dogschema.jsonify(dog), 200)
    
    def put(self, name):
        parser = reqparse.RequestParser()
        parser.add_argument('breed', required=False)
        parser.add_argument('age', type=int, required=False)
        parser.add_argument('available_for_adoption', type=bool, required=False)
        args = parser.parse_args()

        return update_dog(name, args['breed'], args['age'], args['available_for_adoption'])

    def delete(self, name):
        return delete_dog(name)
    
    
api.add_resource(DogResource, '/dogs')
api.add_resource(DogDetails, '/dogs/<id>')
