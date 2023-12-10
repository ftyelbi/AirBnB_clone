#!/usr/bin/python3
"""Defines unittests for models/user.py.

Unittest classes:
    TestUser
"""
import unittest
from models.user import User
from datetime import datetime
from models import storage


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()
        self.user.email = "test@example.com"
        self.user.password = "password123"
        self.user.first_name = "John"
        self.user.last_name = "Doe"

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_user_instantiation(self):
        self.assertIsInstance(self.user, User)
        self.assertIsInstance(self.user, BaseModel)

    def test_user_attributes(self):
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.password, "password123")
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")

    def test_str_representation(self):
        expected_str = "[User] ({}) {}".format(self.user.id, self.user.__dict__)
        self.assertEqual(str(self.user), expected_str)

    def test_to_dict_method(self):
        user_dict = self.user.to_dict()
        self.assertTrue(isinstance(user_dict, dict))
        self.assertEqual(user_dict["id"], self.user.id)
        self.assertEqual(user_dict["email"], self.user.email)
        self.assertEqual(user_dict["password"], self.user.password)
        self.assertEqual(user_dict["first_name"], self.user.first_name)
        self.assertEqual(user_dict["last_name"], self.user.last_name)
        self.assertEqual(user_dict["__class__"], "User")

    def test_to_dict_and_back(self):
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertIsInstance(new_user, User)
        self.assertEqual(new_user.id, self.user.id)
        self.assertEqual(new_user.email, self.user.email)
        self.assertEqual(new_user.password, self.user.password)
        self.assertEqual(new_user.first_name, self.user.first_name)
        self.assertEqual(new_user.last_name, self.user.last_name)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.user.created_at, datetime)
        self.assertIsInstance(self.user.updated_at, datetime)
        self.assertEqual(self.user.created_at, self.user.updated_at)

    def test_save_method(self):
        before_save_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(before_save_updated_at, self.user.updated_at)

if __name__ == "__main__":
    unittest.main()
