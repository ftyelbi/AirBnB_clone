#!/usr/bin/python3
"""Defines unittests for models/amenity.py.

Unittest classes:
    TestAmenity
"""
import unittest
import os
from models.amenity import Amenity
from datetime import datetime
from models import storage


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def tearDown(self):
        storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_amenity_instantiation(self):
        self.assertIsInstance(self.amenity, Amenity)

    def test_attributes_initialization(self):
        self.assertTrue(hasattr(self.amenity, 'id'))
        self.assertTrue(hasattr(self.amenity, 'created_at'))
        self.assertTrue(hasattr(self.amenity, 'updated_at'))
        self.assertTrue(hasattr(self.amenity, 'name'))
        self.assertIsInstance(self.amenity.id, str)
        self.assertIsInstance(self.amenity.created_at, datetime)
        self.assertIsInstance(self.amenity.updated_at, datetime)
        self.assertIsInstance(self.amenity.name, str)

    def test_id_uniqueness(self):
        new_amenity = Amenity()
        self.assertNotEqual(self.amenity.id, new_amenity.id)

    def test_str_representation(self):
        expected_str = "[Amenity] ({}) {}".format(self.amenity.id, self.amenity.__dict__)
        self.assertEqual(str(self.amenity), expected_str)

    def test_to_dict_method(self):
        amenity_dict = self.amenity.to_dict()
        self.assertTrue(isinstance(amenity_dict, dict))
        self.assertEqual(amenity_dict["id"], self.amenity.id)
        self.assertEqual(amenity_dict["__class__"], "Amenity")
        self.assertIsInstance(amenity_dict["created_at"], str)
        self.assertIsInstance(amenity_dict["updated_at"], str)
        self.assertEqual(amenity_dict["name"], self.amenity.name)

    def test_to_dict_and_back(self):
        amenity_dict = self.amenity.to_dict()
        new_amenity = Amenity(**amenity_dict)
        self.assertIsInstance(new_amenity, Amenity)
        self.assertEqual(new_amenity.id, self.amenity.id)
        self.assertEqual(new_amenity.created_at, self.amenity.created_at)
        self.assertEqual(new_amenity.updated_at, self.amenity.updated_at)
        self.assertEqual(new_amenity.name, self.amenity.name)

    def test_save_method(self):
        before_save_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(before_save_updated_at, self.amenity.updated_at)

    def test_save_updates_file(self):
        self.amenity.save()
        with open("file.json", "r") as f:
            content = f.read()
            self.assertIn("Amenity." + self.amenity.id, content)


if __name__ == "__main__":
    unittest.main()
