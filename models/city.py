#!/usr/bin/python3
"""class inherit from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class attributes"""
    state_id = ""
    name = ""
