#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines the FileStorage class."""

import os
import json
from models.place import Place
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.review import Review
from models.state import State
from models.amenity import Amenity


cClass = {'User': User, 'BaseModel': BaseModel,
          'Amenity': Amenity, 'City': City, 'State': State,
          'Place': Place, 'Review': Review}


class FileStorage:
    """Manages storage of JSON file used to store objects."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        ndict = {}
        for key, value in FileStorage.__objects.items():
            ndict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(ndict, f)

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        exists; otherwise, do nothing)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r',
                      encoding='utf-8') as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                class_name = value["__class__"]
                obj = eval(class_name + "(**value)")
                FileStorage.__objects[key] = obj
        else:
            return
