#!/usr/bin/python3
""" This script defines a class FileStorage """
from models.base_model import BaseModel
from os import path
import json


class FileStorage():
    """ This class that serializes instances to a JSON
        file and deserialize JSON file to instances """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This method returns the dictionary __objects """
        return FileStorage.__objects

    def new(self, obj):
        """ This method sets in __objects
            the obj with key <obj class name>.id """
        FileStorage.__objects.update({"{}.{}\
".format(obj.__class__.__name__, obj.id): obj})

    def save(self):
        """ This method serializes __objects
            to the JSON file (path: __file_path) """
        obj = {}
        for key, value in FileStorage.__objects.items():
            obj[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w') as fd:
            json.dump(obj, fd)

    def reload(self):
        """ Deserializes the JSON file
            to __objects (only if the JSON file exists) """
        if path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as fd:
                FileStorage.__objects = json.load(fd)
            for value in FileStorage.__objects.values():
                self.new(eval(value["__class__"])(**value))
