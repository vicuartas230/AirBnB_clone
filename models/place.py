#!/usr/bin/python3
""" This script defines a Place class """
from models.base_model import BaseModel


class Place(BaseModel):
    """  This class inherits from BaseModel.
         Created four public class attributes. """
    city_id = "" # City.id
    user_id = "" # User.id
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = [] # Amenity.id
