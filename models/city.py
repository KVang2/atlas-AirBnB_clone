#!/usr/bin/python3
from models.base_model import BaseModel
"""This class inherits from BaseModel"""


class City(BaseModel):
    """Puplic class attributes"""
    state_id: str = ""
    name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
