#!/usr/bin/python3
"""Defines unittests for models/place.py.

Unittest classes:
    TestPlace
"""
import unittest
from models.place import Place
from datetime import datetime
from models import storage


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place = Place()
        self.place.city_id = "123"
        self.place.user_id = "456"
        self.place.name = "Cozy Cabin"
        self.place.description = "A beautiful cabin in the woods."
        self.place.number_rooms = 3
        self.place.number_bathrooms = 2
        self.place.max_guest = 6
        self.place.price_by_night = 150
        self.place.latitude = 40.7128
        self.place.longitude = -74.0060
        self.place.amenity_ids = ["a1", "a2", "a3"]

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_place_instantiation(self):
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_place_attributes(self):
        self.assertEqual(self.place.city_id, "123")
        self.assertEqual(self.place.user_id, "456")
        self.assertEqual(self.place.name, "Cozy Cabin")
        self.assertEqual(self.place.description, "A beautiful cabin in the woods.")
        self.assertEqual(self.place.number_rooms, 3)
        self.assertEqual(self.place.number_bathrooms, 2)
        self.assertEqual(self.place.max_guest, 6)
        self.assertEqual(self.place.price_by_night, 150)
        self.assertEqual(self.place.latitude, 40.7128)
        self.assertEqual(self.place.longitude, -74.0060)
        self.assertEqual(self.place.amenity_ids, ["a1", "a2", "a3"])

    def test_str_representation(self):
        expected_str = "[Place] ({}) {}".format(self.place.id, self.place.__dict__)
        self.assertEqual(str(self.place), expected_str)

    def test_to_dict_method(self):
        place_dict = self.place.to_dict()
        self.assertTrue(isinstance(place_dict, dict))
        self.assertEqual(place_dict["id"], self.place.id)
        self.assertEqual(place_dict["city_id"], self.place.city_id)
        self.assertEqual(place_dict["user_id"], self.place.user_id)
        self.assertEqual(place_dict["name"], self.place.name)
        self.assertEqual(place_dict["description"], self.place.description)
        self.assertEqual(place_dict["number_rooms"], self.place.number_rooms)
        self.assertEqual(place_dict["number_bathrooms"], self.place.number_bathrooms)
        self.assertEqual(place_dict["max_guest"], self.place.max_guest)
        self.assertEqual(place_dict["price_by_night"], self.place.price_by_night)
        self.assertEqual(place_dict["latitude"], self.place.latitude)
        self.assertEqual(place_dict["longitude"], self.place.longitude)
        self.assertEqual(place_dict["amenity_ids"], self.place.amenity_ids)
        self.assertEqual(place_dict["__class__"], "Place")

    def test_to_dict_and_back(self):
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertIsInstance(new_place, Place)
        self.assertEqual(new_place.id, self.place.id)
        self.assertEqual(new_place.city_id, self.place.city_id)
        self.assertEqual(new_place.user_id, self.place.user_id)
        self.assertEqual(new_place.name, self.place.name)
        self.assertEqual(new_place.description, self.place.description)
        self.assertEqual(new_place.number_rooms, self.place.number_rooms)
        self.assertEqual(new_place.number_bathrooms, self.place.number_bathrooms)
        self.assertEqual(new_place.max_guest, self.place.max_guest)
        self.assertEqual(new_place.price_by_night, self.place.price_by_night)
        self.assertEqual(new_place.latitude, self.place.latitude)
        self.assertEqual(new_place.longitude, self.place.longitude)
        self.assertEqual(new_place.amenity_ids, self.place.amenity_ids)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.place.created_at, datetime)
        self.assertIsInstance(self.place.updated_at, datetime)
        self.assertEqual(self.place.created_at, self.place.updated_at)

    def test_save_method(self):
        before_save_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(before_save_updated_at, self.place.updated_at)

if __name__ == "__main__":
    unittest.main()
