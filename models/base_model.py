#!/usr/bin/python3
""" This script defines a BaseModel class """
from datetime import datetime
import uuid


class BaseModel():
    """ This class contains all common attributes/methods
        for other classes. """
    def __init__(self, *args, **kwargs):
        """ Constructor method to initialize the attribute of the
            instantiated object with one args and kwars """
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'created_at' or key == 'updated_at':
                    convert = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    value = convert
                setattr(self, key, value)
        else:
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
                    updated_at=self.updated_at.isoformat(),
                    __class__=__class__.__name__)
