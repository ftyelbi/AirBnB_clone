#!/usr/bin/python3
"""Defines unittests for models/review.py.

Unittest classes:
    TestReview
"""
import unittest
from models.review import Review
from datetime import datetime
from models import storage


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review = Review()
        self.review.place_id = "123"
        self.review.user_id = "456"
        self.review.text = "Great place!"

    def tearDown(self):
        storage._FileStorage__objects = {}

    def test_review_instantiation(self):
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_review_attributes(self):
        self.assertEqual(self.review.place_id, "123")
        self.assertEqual(self.review.user_id, "456")
        self.assertEqual(self.review.text, "Great place!")

    def test_str_representation(self):
        expected_str = "[Review] ({}) {}".format(self.review.id, self.review.__dict__)
        self.assertEqual(str(self.review), expected_str)

    def test_to_dict_method(self):
        review_dict = self.review.to_dict()
        self.assertTrue(isinstance(review_dict, dict))
        self.assertEqual(review_dict["id"], self.review.id)
        self.assertEqual(review_dict["place_id"], self.review.place_id)
        self.assertEqual(review_dict["user_id"], self.review.user_id)
        self.assertEqual(review_dict["text"], self.review.text)
        self.assertEqual(review_dict["__class__"], "Review")

    def test_to_dict_and_back(self):
        review_dict = self.review.to_dict()
        new_review = Review(**review_dict)
        self.assertIsInstance(new_review, Review)
        self.assertEqual(new_review.id, self.review.id)
        self.assertEqual(new_review.place_id, self.review.place_id)
        self.assertEqual(new_review.user_id, self.review.user_id)
        self.assertEqual(new_review.text, self.review.text)

    def test_created_at_and_updated_at(self):
        self.assertIsInstance(self.review.created_at, datetime)
        self.assertIsInstance(self.review.updated_at, datetime)
        self.assertEqual(self.review.created_at, self.review.updated_at)

    def test_save_method(self):
        before_save_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(before_save_updated_at, self.review.updated_at)

if __name__ == "__main__":
    unittest.main()
