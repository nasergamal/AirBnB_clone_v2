#!/usr/bin/python3
"""unit tests for amenity model"""
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
from os import getenv


class test_Amenity(test_basemodel):
    """Amenity class Unittests """

    a = getenv('HBNB_TYPE_STORAGE') != 'db'

    def __init__(self, *args, **kwargs):
        '''init tests'''
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.name), str)
