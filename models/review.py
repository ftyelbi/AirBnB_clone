#!/usr/bin/python3
"""importing the base_model module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """public attribute that inherits
        from BaseModel
    """
    place_id = ""
    user_id = ""
    text = ""
