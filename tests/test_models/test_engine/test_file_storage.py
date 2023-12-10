#!/usr/bin/python3
"""Defines unittests for models/engine/file_storage.py.

Unittest classes:
    TestFileStorage
"""
import unittest
import os
import json
from models.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import datetime


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_all_method(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new_method(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.assertIn(f"BaseModel.{bm.id}", self.storage.all())

    def test_save_method(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        with open("file.json", "r") as f:
            content = json.load(f)
            self.assertIn(f"BaseModel.{bm.id}", content)

    def test_reload_method(self):
        bm = BaseModel()
        self.storage.new(bm)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{bm.id}", self.storage.all())

    def test_classes_method(self):
        classes = self.storage.classes()
        self.assertIsInstance(classes, dict)
        self.assertEqual(classes["BaseModel"], BaseModel)
        self.assertEqual(classes["User"], User)
        self.assertEqual(classes["State"], State)
        self.assertEqual(classes["City"], City)
        self.assertEqual(classes["Amenity"], Amenity)
        self.assertEqual(classes["Place"], Place)
        self.assertEqual(classes["Review"], Review)

    def test_attributes_method(self):
        attributes = self.storage.attributes()
        self.assertIsInstance(attributes, dict)
        self.assertEqual(attributes["BaseModel"]["id"], str)
        self.assertEqual(attributes["BaseModel"]["created_at"], datetime.datetime)
        self.assertEqual(attributes["BaseModel"]["updated_at"], datetime.datetime)
        self.assertEqual(attributes["User"]["email"], str)
        self.assertEqual(attributes["User"]["password"], str)
        self.assertEqual(attributes["User"]["first_name"], str)
        self.assertEqual(attributes["User"]["last_name"], str)

    def test_reload_nonexistent_file(self):
        # Test reload when the file doesn't exist
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_reload_invalid_file_content(self):
        # Test reload with an invalid JSON file content
        with open("file.json", "w") as f:
            f.write("invalid json content")
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})

    def test_attributes_contains_valid_values(self):
        attributes = self.storage.attributes()
        self.assertEqual(attributes["Place"]["number_rooms"], int)
        self.assertEqual(attributes["Place"]["number_bathrooms"], int)
        self.assertEqual(attributes["Place"]["max_guest"], int)
        self.assertEqual(attributes["Place"]["price_by_night"], int)
        self.assertEqual(attributes["Place"]["latitude"], float)
        self.assertEqual(attributes["Place"]["longitude"], float)
        self.assertEqual(attributes["Place"]["amenity_ids"], list)


if __name__ == "__main__":
    unittest.main()
