#!/usr/bin/python3
"""
FileStorage module for serializing and deserializing BaseModel instances
"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Class that serializes and deserializes instances to and from a JSON file"""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(
                {key: obj.to_dict() for key, obj in FileStorage.__objects.items()},
                file
            )

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                objects = json.load(file)
                for key, obj in objects.items():
                    cls_name = key.split('.')[0]
                    if cls_name == 'BaseModel':
                        obj_instance = BaseModel(**obj)
                        FileStorage.__objects[key] = obj_instance
