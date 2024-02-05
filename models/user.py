#!/usr/bin/python3
"""User file"""
from models.base_model import BaseModel


class User(BaseModel):
    """class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User Instance"""
        super().__init__(*args, **kwargs)
