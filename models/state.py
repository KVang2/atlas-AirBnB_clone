#!/usr/bin/python3
from models.base_model import BaseModel
"""
This class inheret from BaseModel
"""


class State(BaseModel):
    """State class attributes"""
    def __init__(self, *args, **kwargs):
        """Initialize State Instance"""
        name = ""
