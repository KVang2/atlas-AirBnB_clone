#!/usr/bin/python3
from models import storage
import uuid
from datetime import datetime
"""
BaseModel class
"""


class BaseModel:
    """
    Base class for other models in the application.

    Attributes:
        - id (str): Unique identifier for each instance.
        - created_at (datetime): Date and time when the instance is created.
        - updated_at (datetime): Date and time when the instance is last updated.

    Methods:
        - __init__: Initializes a new instance of the BaseModel.
        - __str__: Returns a string representation of the BaseModel instance.
        - save: Updates the `updated_at` attribute and saves the instance.
        - to_dict: Converts the instance to a dictionary representation.

    Usage:
        This class serves as the foundation for other model classes, providing common attributes
        and methods such as creating, saving, and converting instances to dictionaries.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel.

        Args:
            *args: Variable length argument list (unused in this implementation).
            **kwargs: Keyword arguments to create an instance or initialize attributes.

        If `kwargs` is provided:
            - It iterates through the key-value pairs and sets the instance attributes accordingly.
            - Converts string representations of 'created_at' and 'updated_at' to datetime objects.
            - Generates a new 'id' if not provided in `kwargs`.
            - Calls `storage.new(self)` to link new instances to storage.

        If `kwargs` is empty:
            - Generates a new 'id', 'created_at', and 'updated_at' for a new instance.
            - Calls `storage.new(self)` to link new instances to storage.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if 'created_at' not in kwargs:
                self.created_at = datetime.now()
            if 'updated_at' not in kwargs:
                self.updated_at = datetime.now()
        else:
            # Creating a new instance with default values
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)  # Call new(self) on storage for new instances

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
            str: A formatted string containing the class name, id, and instance attributes.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the `updated_at` attribute and saves the instance.

        Calls `storage.save(self)` to save the instance using the storage system.
        """
        self.updated_at = datetime.now()
        storage.save(self)  # Call save(self) method of storage

    def to_dict(self):
        """
        Converts the instance to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance attributes in a serializable format.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['__class__'] = self.__class__.__name__
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        return instance_dict

from models import storage

