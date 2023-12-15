#!/usr/bin/python3
"""importing the base_model module"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    public attribute that inherits BaseModel
    """
    state_id = ""
    name = ""
