from api import mongo
from ..models import dog_model
from bson import ObjectId

class DogService:
    def get_all_dogs():
        dogs = mongo.db.dogs.find()
        return [{'name': dog['name'], 'breed': dog['breed'], 'age': dog['age'], 'available_for_adoption': dog['available_for_adoption']} for dog in dogs]

    def get_dog_by_name(name):
        dog = mongo.db.dogs.find_one({'name': name})
        if dog:
            return {'name': dog['name'], 'breed': dog['breed'], 'age': dog['age'], 'available_for_adoption': dog['available_for_adoption']}
        return {'message': 'Dog not found'}, 404

    def create_dog(name, breed, age, available_for_adoption):
        mongo.db.dogs.insert_one({'name': name, 'breed': breed, 'age': age, 'available_for_adoption': available_for_adoption})
        return {'message': 'Dog created successfully'}, 201

    def update_dog(name, breed=None, age=None, available_for_adoption=None):
        update_fields = {}
        if breed:
            update_fields['breed'] = breed
        if age:
            update_fields['age'] = age
        if available_for_adoption is not None:
            update_fields['available_for_adoption'] = available_for_adoption
        
        result = mongo.db.dogs.update_one({'name': name}, {'$set': update_fields})
        if result.matched_count:
            return {'message': 'Dog updated successfully'}
        return {'message': 'Dog not found'}, 404

    def delete_dog(name):
        result = mongo.db.dogs.delete_one({'name': name})
        if result.deleted_count:
            return {'message': 'Dog deleted successfully'}
        return {'message': 'Dog not found'}, 404