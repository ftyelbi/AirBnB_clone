#!/usr/bin/python3

"""
    Tests for BaseModel class
"""

import unittest
from models.base_model import BaseModel
from io import StringIO
import sys
import datetime


class TestBase(unittest.TestCase):
    """
        Testing the methods and parameters for
        BaseModel class
    """
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "Nii Fty"

    def TearDown(self):
        del self.my_model

    def test_id_type(self):
        self.assertEqual("<class 'str'>", str(type(self.my_model.id)))

    def test_ids_differ(self):
        new_model = BaseModel()
        self.assertNotEqual(new_model.id, self.my_model.id)

    def test_name(self):
        self.assertEqual("Nii Fty", self.my_model.name)

    def test_a_updated_created_equal(self):
        self.assertEqual(self.my_model.updated_at.year,
                         self.my_model.created_at.year)

    def test_save(self):
        old_update = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_update)

    def test_str_override(self):
        backup = sys.stdout
        instance_id = self.my_model.id
        capture_out = StringIO()
        sys.stdout = capture_out
        print(self.my_model)

        cap = capture_out.getvalue().split(" ")
        self.assertEqual(cap[0], "[BaseModel]")

        self.assertEqual(cap[1], "({})".format(instance_id))
        sys.stdout = backup

    def test_to_dict_type(self):
        self.assertEqual("<class 'dict'>",
                         str(type(self.my_model.to_dict())))

    def test_to_dict_class(self):
        self.assertEqual("BaseModel", (self.my_model.to_dict())["__class__"])

    def test_to_dict_type_updated_at(self):
        self.assertEqual("<class 'str'>",
                         str(type((self.my_model.to_dict())["updated_at"])))

    def test_to_dict_type_created_at(self):

        tmp = self.my_model.to_dict()
        self.assertEqual("<class 'str'>", str(type(tmp["created_at"])))

    def test_kwargs_instantiation(self):
        mode_dict = self.my_model.to_dict()
        new_model = BaseModel(**mode_dict)
        self.assertEqual(new_model.id, self.my_model.id)

    def test_type_created_at(self):
        mode_dict = self.my_model.to_dict()
        new_model = BaseModel(mode_dict)
        self.assertTrue(isinstance(new_model.created_at, datetime.datetime))

    def test_updated_at_type(self):
        mode_dict = self.my_model.to_dict()
        new_model = BaseModel(mode_dict)
        self.assertTrue(isinstance(new_model.updated_at, datetime.datetime))

    def test_compare_dict(self):
        mode_dict = self.my_model.to_dict()
        new_model = BaseModel(**mode_dict)
        new_model_dict = new_model.to_dict()
        self.assertEqual(mode_dict, new_model_dict) 
