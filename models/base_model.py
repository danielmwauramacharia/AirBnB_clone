##!/usr/bin/python3
"""The base model module"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Defining the properties of the base model"""

    def __init__(self, *args, **kwrgs):
        """Attributes instantiation"""
        if kwrgs:
            for key, value in kwrgs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at', ] and isinstance(key, str):
                    value = datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self) -> str:
        """Return the string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the updated at attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the attributes of object to dictionary"""
        to_json = self.__dict__
        to_json['__class__'] = self.__class__.__name__
        to_json['created_at'] = to_json['created_at'].isoformat()
        to_json['updated_at'] = to_json['updated_at'].isoformat()
        return to_json
