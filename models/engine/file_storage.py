#!/usr/bin/python3
"""
FileStorage class to handle serialization and deserialization
"""
import json
from models.base_model import BaseModel
from models.user import User

class FileStorage:
    """FileStorage class"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary of objects"""
        return self.__objects

    def new(self, obj):
        """Adds a new object to the storage"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves the objects to a JSON file"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Reloads objects from the JSON file"""
        try:
            with open(self.__file_path, 'r') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name = value['__class__']
                    if cls_name == 'BaseModel':
                        obj = BaseModel(**value)
                    elif cls_name == 'User':
                        obj = User(**value)
                    # Add more elif blocks here for other classes
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
