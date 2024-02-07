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

        # If keyword arguments exist or passed instantiation 
        if kwargs:
            for key, value in kwargs.items(): # Iterate through each key-value
                # Checking key then convert value to datetime obj
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != '__class__':
                    setattr(self, key, value)
                    # Set attribute with key as name and value as its value
    
        else:
            # If no kwargs, make new UUID for id
            self.id = str(uuid.uuid4())
            # Set both attribute to current datetime
            self.created_at = self.updated_at = datetime.now()
            # Add new instance to storage
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
