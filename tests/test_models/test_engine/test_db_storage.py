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
import MySQLdb


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

    def test_delete_new(self):
        '''test delete function'''
        s = len((storage.all()).keys())
        st = State(name="Delh")
        self.assertFalse(st in storage.all().values())
        storage.new(st)
        storage.save()
        self.assertTrue(st in storage.all().values())
        s2 = len((storage.all()).keys())
        self.assertEqual(s + 1, s2)
        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            password=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB'))
        c = db.cursor()
        c.execute(f"SELECT * from states WHERE id ='{st.id}'")
        r = c.fetchone()
        self.assertTrue(st is not None)
        self.assertTrue(st.name == "Delh")
        storage.delete(st)
        s2 = len((storage.all()).keys())
        self.assertEqual(s, s2)
        c.close()
        db.close()

    def test_fake_delete(self):
        '''test delete function'''
        with self.assertRaises(sqlalchemy.exc.InvalidRequestError):
            storage.delete(State(name="Delh"))

    def test_reload(self):
        '''unit tests for reload function'''
        db = MySQLdb.connect(
            host=os.getenv('HBNB_MYSQL_HOST'),
            port=3306,
            user=os.getenv('HBNB_MYSQL_USER'),
            password=os.getenv('HBNB_MYSQL_PWD'),
            db=os.getenv('HBNB_MYSQL_DB'))
        c = db.cursor()
        t = '2023-08-21T01:27:15.787197'
        s = 'unique-id'
        cm = f"INSERT INTO states(id, name, created_at, updated_at)\
              VALUES('{s}', 'Deh', '{t}', '{t}');"
        c.execute(cm)
        self.assertNotIn('State.unique-id', storage.all())
        db.commit()
        storage.reload()
        self.assertIn('State.unique-id', storage.all())
        c.close()
        db.close()
