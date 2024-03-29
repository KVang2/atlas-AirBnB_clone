#!/usr/bin/python3
import uuid
from datetime import datetime
import models
"""
class Base Model
"""


class BaseModel:
    def __init__(self, *args, **kwargs):
        """Initialize BaseModel instance."""
        from models import storage

        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Return a string representation
        of the instance."""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Update the public instance attribute
        updated_at with the current datetime."""
        from models import storage
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Return a dictionary containing
        all keys/values of __dict__ of the instance."""
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
