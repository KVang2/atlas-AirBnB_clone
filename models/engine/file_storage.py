#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
"""
This class represents the serialization and
deserialization of a file
"""


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    Classes = {
        'BaseModel': BaseModel,
        'User': User,
        'BaseModel': BaseModel,
        'State': State,
        'City': City,
        'Amenity': Amenity
    }

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, obj_dict in data.items():
                    class_name, _ = key.split('.')
                    obj_instance = self.Classes[class_name](**obj_dict)
                    self.__objects[key] = obj_instance
        except FileNotFoundError:
            pass  # No exception should be raised if the file doesn't exist
