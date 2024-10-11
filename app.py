from api import app, mongo
from api.models.dog_model import Dog
from api.services.dog_service import DogService

if __name__ == '__main__':
    with app.app_context():
        if 'dogs' not in mongo.db.list_collection_names():
            dog = Dog(
                name='',
                breed='',
                age=0,
                available_for_adoption=False
            )
            DogService.create_dog(dog.name, dog.breed, dog.age, dog.available_for_adoption)
    app.run(port=5000, debug=True)