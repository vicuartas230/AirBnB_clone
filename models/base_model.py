#!/usr/bin/python3
""" This script defines all common attributes/methods for other classes. """
from datetime import datetime
import uuid


class BaseModel():
    def __init__(self, id=0, created_at=None, updated_at=None):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        return "[{}] ({}) {}".format(__class__.__name__, self.id, self.__dict__)

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self):
        return dict(my_number=getattr(self, "my_number"), name=getattr(self, "name"), id=self.id, created_at=self.created_at.isoformat(), update_at=self.updated_at.isoformat(), __class__=__class__.__name__)
