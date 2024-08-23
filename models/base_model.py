#!/usr/bin/python3
"""The base model module"""
from uuid import uuid4
from datetime import datetime
# import models


class BaseModel:
    """Defining the properties of the base model"""

    def __init__(self, *args, **kwrgs):
        """Attributes instantiation"""
        if args:
            pass
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwrgs:
            for key, value in kwrgs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            # models.storage.new(self)

    def save(self):
        """Update the updated at attribute"""
        self.updated_at = datetime.now()
        # models.storage.save()

    def to_dict(self):
        """Convert the attributes of object to dictionary"""
        to_dict = self.__dict__.copy()
        to_dict['__class__'] = self.__class__.__name__
        to_dict['created_at'] = self.created_at.isoformat()
        to_dict['updated_at'] = self.updated_at.isoformat()
        return to_dict

    def __str__(self) -> str:
        """Return the string representation of the object"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
