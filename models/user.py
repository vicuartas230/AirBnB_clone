#!/usr/bin/python3
""" This script defines a User class """
from models.base_model import BaseModel


class User(BaseModel):
    """  This class inherits from BaseModel.
         Created four public class attributes. """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
