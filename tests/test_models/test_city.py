#!/usr/bin/python3
"""Defines unittests for models/city.py.

Unittest classes:
    TestCity
"""
import unittest
from models.city import City
from datetime import datetime
from models import storage


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city = City()
        self.city.state_id = "123"
        self.city.name = "Springfield"

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_city_instantiation(self):
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_city_attributes(self):
        self.assertEqual(self.city.state_id, "123")
        self.assertEqual(self.city.name, "Springfield")

    def test_str_representation(self):
        expected_str = "[City] ({}) {}".format(self.city.id, self.city.__dict__)
        self.assertEqual(str(self.city), expected_str)

    def test_to_dict_method(self):
        city_dict = self.city.to_dict()
        self.assertTrue(isinstance(city_dict, dict))
        self.assertEqual(city_dict["id"], self.city.id)
        self.assertEqual(city_dict["state_id"], self.city.state_id)
        self.assertEqual(city_dict["name"], self.city.name)
        self.assertEqual(city_dict["__class__"], "City")

    def test_to_dict_and_back(self):
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertIsInstance(new_city, City)
        self.assertEqual(new_city.id, self.city.id)
        self.assertEqual(new_city.state_id, self.city.state_id)
        self.assertEqual(new_city.name, self.city.name)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.city.created_at, datetime)
        self.assertIsInstance(self.city.updated_at, datetime)
        self.assertEqual(self.city.created_at, self.city.updated_at)

    def test_save_method(self):
        before_save_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(before_save_updated_at, self.city.updated_at)

if __name__ == "__main__":
    unittest.main()
