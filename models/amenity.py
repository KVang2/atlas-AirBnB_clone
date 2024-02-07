#!/usr/bin/python3
from models.base_model import BaseModel
"""Amenity class inherits from BaseModel"""


class Amenity(BaseModel):
    """Amenity Class attributes"""
    name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
