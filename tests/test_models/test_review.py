#!/usr/bin/python3
"""unit tests for review model"""
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from os import getenv


class test_review(test_basemodel):
    """Review Class unit tests"""

    a = getenv('HBNB_TYPE_STORAGE') != 'db'

    def __init__(self, *args, **kwargs):
        """init tests"""
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.place_id), str)

    def test_user_id(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.user_id), str)

    def test_text(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.text), str)
