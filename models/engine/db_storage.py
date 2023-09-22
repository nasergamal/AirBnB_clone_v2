#!/usr/bin/python3
'''database type storage'''
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    '''dbstorage class manages storage of models in mysql'''

    __engine = None
    __session = None
    __classes = [City, State, User, Place, Review, Amenity]

    def __init__(self):
        '''linking engine to database'''
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(
                                               getenv('HBNB_MYSQL_USER'),
                                               getenv('HBNB_MYSQL_PWD'),
                                               getenv('HBNB_MYSQL_HOST'),
                                               getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''
        return objects depending on the class name (cls)
        or all objects if no argument was given
        '''
        dictionary = {}
        if cls:
            query = self.__session.query(cls)
            for row in query:
                dictionary[f'{row.__class__.__name__}.{row.id}'] = row
        else:
            for c in self.__classes:
                query = self.__session.query(c)
                for row in query:
                    dictionary[f'{row.__class__.__name__}.{row.id}'] = row
        return dictionary

    def new(self, obj):
        '''add new object to session to database'''
        self.__session.add(obj)

    def save(self):
        '''save changes to database'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete object from database'''
        if obj:
            self.__session.delete(obj)

    def reload(self):
        '''initialize session'''
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(session)()

    def close(self):
        '''restart'''
        self.__session.close()
