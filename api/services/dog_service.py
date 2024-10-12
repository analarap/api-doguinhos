from api import mongo
from ..models import dog_model
from bson import ObjectId

class DogService:
    @staticmethod
    def get_all_dogs():
        dogs = list(mongo.db.dogs.find())
        if dogs:
            return [{'id': str(dog['_id']), 'name': dog['name'], 'breed': dog['breed'], 'age': dog['age'], 'available_for_adoption': dog['available_for_adoption']} for dog in dogs]
        return {'message': 'No dogs found'}, 404

    @staticmethod
    def get_dog_by_id(id):
        dog = mongo.db.dogs.find_one({'_id': ObjectId(id)})
        if dog:
            return {'id': str(dog['_id']), 'name': dog['name'], 'breed': dog['breed'], 'age': dog['age'], 'available_for_adoption': dog['available_for_adoption']}
        return {'message': 'Dog not found'}, 404

    @staticmethod
    def create_dog(name, breed, age, available_for_adoption):
        result = mongo.db.dogs.insert_one({
            'name': name, 
            'breed': breed, 
            'age': age, 
            'available_for_adoption': available_for_adoption
        })
        return {'message': f'Dog created successfully (id: {result.inserted_id})'}, 201

    @staticmethod
    def update_dog(id, name=None, breed=None, age=None, available_for_adoption=None):
        update_fields = {}
        if name:
            update_fields['name'] = name
        if breed:
            update_fields['breed'] = breed
        if age is not None:
            update_fields['age'] = age
        if available_for_adoption is not None:
            update_fields['available_for_adoption'] = available_for_adoption

        updated_dog = mongo.db.dogs.find_one_and_update(
            {'_id': ObjectId(id)},
            {'$set': update_fields},
            return_document=True
        )
        
        if updated_dog:
            return {'id': str(updated_dog['_id']), 'name': updated_dog['name'], 'breed': updated_dog['breed'], 'age': updated_dog['age'], 'available_for_adoption': updated_dog['available_for_adoption']}
        
        return {'message': 'Dog not found'}, 404

    @staticmethod
    def delete_dog(id):
        result = mongo.db.dogs.delete_one({'_id': ObjectId(id)})
        if result.deleted_count:
            return {"message": "Dog successfully deleted"}
        return {"message": "Dog not found"}, 404