#!/usr/bin/python3
"""unit tests for state model"""
from tests.test_models.test_base_model import test_basemodel
from models.state import State
from os import getenv


class test_state(test_basemodel):
    """State Class unit tests" """

    a = getenv('HBNB_TYPE_STORAGE') != 'db'

    def __init__(self, *args, **kwargs):
        """Init tests"""
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        new = self.value()
        if self.a:
            self.assertEqual(type(new.name), str)
