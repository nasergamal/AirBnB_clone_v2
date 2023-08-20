#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# from models import storage_method
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if models.storage_method == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ""

    @property
    def cities(self):
        '''return a list of cities in a state'''
        cities_list = []
        all_cities = models.storage.all(City)
        for city in all_cities.values():
            if self.id == city.state_id:
                cities_list.append(city)
        return cities_list
