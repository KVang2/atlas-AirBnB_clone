#!/usr/bin/python3
"""Class inherit from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """State class attributes"""
    def __init__(self, *args, **kwargs):
        """Initialize State Instance"""
        super().__init__(*args, **kwargs)
        name = ""
