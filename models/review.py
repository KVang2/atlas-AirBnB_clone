#!/usr/bin/python3
from models.base_model import BaseModel
"""This class inherits from BaseModel"""


class Review(BaseModel):
    """Puplic class attributes"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
