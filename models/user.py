#!/usr/bin/python3
from models.base_model import BaseModel
"""
User class inheret from BaseModel
"""


class User(BaseModel):
    """class inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize User Instance"""
        super().__init__(*args, **kwargs)
