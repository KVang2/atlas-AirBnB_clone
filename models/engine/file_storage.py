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
    """FileStorage for storing and retrieving obj to/from JSON file"""
    __file_path = "file.json" # Set path to the JSON file
    __objects = {} # Dictionary to store objects

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
        key = "{}.{}".format(obj.__class__.__name__, obj.id) # Creating key using class name and obj id
        self.__objects[key] = obj # Adding obj to obj dictionary

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        serialized_objects = {} #Dictionary to store serialized obj
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, 'w') as file:
            json.dump(serialized_objects, file) # Write serialized obj to file as JSON

    def reload(self):
        """Deserializes the JSON file to __objects."""
        from models.base_model import BaseModel
        try:
            with open(self.__file_path, 'r') as file: # Open file in read mode
                data = json.load(file) # Load JSON data from file
                for key, obj_dict in data.items(): # Iterate through obj in JSON data
                    class_name, _ = key.split('.') # Extract class name from key
                    obj_instance = self.Classes[class_name](**obj_dict) # Create instance of corresponding class
                    self.__objects[key] = obj_instance # Add obj to __obj dict
        except FileNotFoundError:
            pass  # No exception should be raised if the file doesn't exist
