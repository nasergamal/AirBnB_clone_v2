#!/usr/bin/python3
""" Module for testing db storage"""
import unittest
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import sqlalchemy
from models import storage
import os


@unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db', 'db test')
class test_DbStorage(unittest.TestCase):
    '''db storage unit tests'''

    def test_obj_all_with_arg(self):
        ''' compare all function with vs without'''
        s1 = State(name="Cal")
        s2 = State(name="Di")
        storage.new(s1)
        storage.new(s2)
        storage.save()
        storage.new(City(state_id=s1.id, name='san Francisco'))
        storage.new(City(state_id=s2.id, name='names'))
        storage.save()
        self.assertNotEqual(len(storage.all().keys()),
                            len(storage.all(State).keys()))
        objs = storage.all(State)
        for v in objs.values():
            self.assertTrue(v.__class__.__name__ == 'State')

    def test_obj_list_two(self):
        """ correct storage test """
        s = len((storage.all()).keys())
        storage.new(State(name="California"))
        storage.new(State(name="Delhi"))
        storage.save()
        self.assertEqual(len(storage.all().keys()), s + 2)

    def test_delete(self):
        '''test delete function'''
        s = len((storage.all()).keys())
        st = State(name="Delh")
        storage.new(st)
        storage.save()
        s2 = len((storage.all()).keys())
        self.assertEqual(s + 1, s2)
        storage.delete(st)
        s2 = len((storage.all()).keys())
        self.assertEqual(s, s2)

    def test_fake_delete(self):
        '''test delete function'''
        with self.assertRaises(sqlalchemy.exc.InvalidRequestError):
            storage.delete(State(name="Delh"))
