#!/usr/bin/python3
"""unit tests for User model"""
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from os import getenv


class test_User(test_basemodel):
    """User Class unit tests"""
    a = getenv('HBNB_TYPE_STORAGE') != 'db'

    def __init__(self, *args, **kwargs):
        """init tests"""
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.first_name), str)

    def test_last_name(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.last_name), str)

    def test_email(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.email), str)

    def test_password(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.password), str)
