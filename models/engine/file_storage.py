#!/usr/bin/python3
import json

class FileStorage:
    __file_path = "storage.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def classes(self):
        """Returns a dictionary of classes"""
        from models.base_model import BaseModel
        from models.user import User
        from models.review import Review
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        classes = {
                'BaseModel': BaseModel,
                'User': User,
                'Review': Review,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place
                }
        return classes

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        serialized_objects = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(serialized_objects, f)

    def reload(self):
        """Deserializes JSON file to instances and stores in __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                data = {key: self.classes()[value["__class__"]](**value)
                        for key, value in data.items()}
                FileStorage.__objects = data
        except FileNotFoundError:
            pass

