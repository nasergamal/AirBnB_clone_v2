#!/usr/bin/python3
"""unittests for city model"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from os import getenv


class test_City(test_basemodel):
    """City Class unit tests"""
    a = getenv('HBNB_TYPE_STORAGE') != 'db'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        '''init tests'''
        self.name = "City"
        self.value = City

    def test_state_id(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.state_id), str)

    def test_name(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.name), str)
