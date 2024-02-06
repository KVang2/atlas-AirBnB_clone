#!/usr/bin/python3
from models.base_model import BaseModel
"""
This class inherits from BaseModel
"""


class State(BaseModel):
    """Puplic class attributes"""
    name: str = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
