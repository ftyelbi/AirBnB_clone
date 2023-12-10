#!/usr/bin/python3
"""Defines unittests for models/base_model.py.

Unittest classes:
    TestBaseModel
"""
import unittest
import os
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def tearDown(self):
        storage._FileStorage__objects = {}
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_base_model_instantiation(self):
        self.assertIsInstance(self.base_model, BaseModel)

    def test_attributes_initialization(self):
        self.assertTrue(hasattr(self.base_model, 'id'))
        self.assertTrue(hasattr(self.base_model, 'created_at'))
        self.assertTrue(hasattr(self.base_model, 'updated_at'))
        self.assertIsInstance(self.base_model.id, str)
        self.assertIsInstance(self.base_model.created_at, datetime)
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_id_uniqueness(self):
        new_base_model = BaseModel()
        self.assertNotEqual(self.base_model.id, new_base_model.id)

    def test_str_representation(self):
        expected_str = "[BaseModel] ({}) {}".format(self.base_model.id, self.base_model.__dict__)
        self.assertEqual(str(self.base_model), expected_str)

    def test_to_dict_method(self):
        base_model_dict = self.base_model.to_dict()
        self.assertTrue(isinstance(base_model_dict, dict))
        self.assertEqual(base_model_dict["id"], self.base_model.id)
        self.assertEqual(base_model_dict["__class__"], "BaseModel")
        self.assertIsInstance(base_model_dict["created_at"], str)
        self.assertIsInstance(base_model_dict["updated_at"], str)

    def test_to_dict_and_back(self):
        base_model_dict = self.base_model.to_dict()
        new_base_model = BaseModel(**base_model_dict)
        self.assertIsInstance(new_base_model, BaseModel)
        self.assertEqual(new_base_model.id, self.base_model.id)
        self.assertEqual(new_base_model.created_at, self.base_model.created_at)
        self.assertEqual(new_base_model.updated_at, self.base_model.updated_at)

    def test_save_method(self):
        before_save_updated_at = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(before_save_updated_at, self.base_model.updated_at)

    def test_save_updates_file(self):
        self.base_model.save()
        with open("file.json", "r") as f:
            content = f.read()
            self.assertIn("BaseModel." + self.base_model.id, content)


if __name__ == "__main__":
    unittest.main()
