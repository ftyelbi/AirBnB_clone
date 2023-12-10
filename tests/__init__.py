#!/usr/bin/python3
"""Initialize the package"""

from models.engine.file_storage import FileStorage

def initialize_package():
    """Initialize the package by setting up storage"""
    storage = FileStorage()
    storage.reload()

if __name__ == "__main__":
    initialize_package()
