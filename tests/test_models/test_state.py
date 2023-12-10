#!/usr/bin/python3
"""Defines unittests for models/state.py.

Unittest classes:
    TestState
"""
import unittest
from models.state import State
from datetime import datetime
from models import storage


class TestState(unittest.TestCase):
    def setUp(self):
        self.state = State()
        self.state.name = "California"

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_state_instantiation(self):
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_state_attributes(self):
        self.assertEqual(self.state.name, "California")

    def test_str_representation(self):
        expected_str = "[State] ({}) {}".format(self.state.id, self.state.__dict__)
        self.assertEqual(str(self.state), expected_str)

    def test_to_dict_method(self):
        state_dict = self.state.to_dict()
        self.assertTrue(isinstance(state_dict, dict))
        self.assertEqual(state_dict["id"], self.state.id)
        self.assertEqual(state_dict["name"], self.state.name)
        self.assertEqual(state_dict["__class__"], "State")

    def test_to_dict_and_back(self):
        state_dict = self.state.to_dict()
        new_state = State(**state_dict)
        self.assertIsInstance(new_state, State)
        self.assertEqual(new_state.id, self.state.id)
        self.assertEqual(new_state.name, self.state.name)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.state.created_at, datetime)
        self.assertIsInstance(self.state.updated_at, datetime)
        self.assertEqual(self.state.created_at, self.state.updated_at)

    def test_save_method(self):
        before_save_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(before_save_updated_at, self.state.updated_at)

if __name__ == "__main__":
    unittest.main()
