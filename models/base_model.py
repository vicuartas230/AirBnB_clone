#!/usr/bin/python3
""" This script defines a BaseModel class """
from datetime import datetime
import uuid
import models


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
            models.storage.new(self)

    def __str__(self):
        """ This method returns a string representation of the instance """
        return "[{}] ({}) {}\
".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        """ This method updates the date of modification """
        models.storage.new(self)
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """ This method returns a dictionary with the instance attributes """
        new = {}
        new.update({'__class__': self.__class__.__name__})
        current = self.__dict__
        for key, value in current.items():
            if key == 'created_at' or key == 'updated_at':
                new.update({key: getattr(self, key).isoformat()})
            else:
                new.update({key: value})
        return new
