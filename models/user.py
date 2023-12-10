#!/usr/bin/python3
"""A class User that inherits from BaseModel"""
from models.base_model import BaseModel

class User(BaseModel):
    """public class attributes for user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
