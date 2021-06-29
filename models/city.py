#!/usr/bin/python3
""" This script defines a City class """
from models.base_model import BaseModel


class City(BaseModel):
    """  This class inherits from BaseModel.
         Created four public class attributes. """
    state_id = "" # State.id
    name = ""
