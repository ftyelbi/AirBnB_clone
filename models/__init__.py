#!/usr/bin/python3
<<<<<<< HEAD
"""Initialize the package"""

from models.engine.file_storage import FileStorage

def initialize_package():
    """Initialize the package by setting up storage"""
    storage = FileStorage()
    storage.reload()

if __name__ == "__main__":
    initialize_package()
=======
"""Importing FileStorage class"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
>>>>>>> a0a74dac5c5b0be75fdab82799df73b82eae9c85
