#!/usr/bin/python3
""" This script defines a BaseModel class """
from datetime import datetime
import uuid


class BaseModel():
    """ This class contains all common attributes/methods
        for other classes. """
    def __init__(self, id=0, created_at=None, updated_at=None):
        """ Constructor method to initialize the attribute of the
            instantiated object with one parameter:

            Parameter:

                id (integer): Is a public instance attribute
                created_at (datetime): Is a public instance attribute
                updated_at (datetime): Is a public instance attribute """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ This method returns a string representation of the instance """
        return "[{}] ({}) {}\
".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ This method updates the date of modification """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ This method returns a dictionary with the instance attributes """
        return dict(my_number=getattr(self, "my_number"),
                    name=getattr(self, "name"), id=self.id,
                    created_at=self.created_at.isoformat(),
                    update_at=self.updated_at.isoformat(),
                    __class__=__class__.__name__)
