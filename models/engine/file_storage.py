#!/usr/bin/python3
"""Module : FileStorage"""
import json
import os
from models.base_model import BaseModel


class FileStorage:
    """Defines the serialization and deserialization of an object"""
    CLASSES = {'BaseModel': BaseModel}
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """make the private class attribute available"""
        return self.__objects

    def new(self, obj):
        """creates a new set of attributes based on the obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialization: Persist data to the json file"""
        serialize_obj = {}
        for key, value in self.__objects.items():
            serialize_obj[key] = value.to_dict()
        with open(self.__file_path, mode="w", encoding="utf-8") as file:
            json.dump(serialize_obj, file)

    def reload(self):
        """deserialize data stored as JSON"""
        if os.path.exists(self.__file_path) and os.path.getsize(self.__file_path) > 0:
            with open(self.__file_path, mode="r", encoding="utf-8") as file:
                content = json.load(file)
                for key, value in content.items():
                    class_name = value['__class__']
                    if class_name in self.CLASSES:
                        instance = self.CLASSES[class_name](**value)
                        self.__objects[key] = instance
