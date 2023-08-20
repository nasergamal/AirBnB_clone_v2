#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_method
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    '''Amenity class'''
    __tablename__ = 'amenities'
    if storage_method == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
