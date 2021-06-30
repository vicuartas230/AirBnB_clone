#!/usr/bin/python3
""" This script defines a Review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """  This class inherits from BaseModel.
    Created three public class attributes. """

    place_id = ""
    user_id = ""
    text = ""
