from api import mongo

class Dog():
    def __init__(self, name, breed, age, available_for_adoption):
        self.name = name
        self.breed = breed
        self.age = age
        self.available_for_adoption = available_for_adoption