#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.amenity import Amenity
from models.review import Review
import models

if models.storage_method == 'db':
    meta = Base.metadata
    place_amenity = Table('place_amenity', meta,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True, nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if models.storage_method == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', backref='place',
                               cascade='all, delete, delete-orphan')
        amenities = relationship('Amenity', secondary=place_amenity,
                                 backref='place-amenity', viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

    @property
    def reviews(self):
        '''return a list of reviews linked to place'''
        review_list = []
        rev = models.storage.all(Review)
        for row in rev.values():
            if row.place_id == self.id:
                review_list.append(row)
        return review_list

    if models.storage_method != 'db':
        @property
        def amenities(self, obj):
            '''set amenities'''
            if obj and isinstance(obj, Amenity) and obj.id and\
               obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)

    if models.storage_method != 'db':
        @property
        def amenities(self):
            '''get amenities'''
            amenities_list = []
            am = models.storage.all(Amenity)
            for row in am.values():
                if row.id == self.amenity_ids:
                    li.append(row)
            return amenities_list
