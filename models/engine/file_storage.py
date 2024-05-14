#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""This module defines a class to manage file storage for hbnb project"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """This class manages storage of JSON file"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, mode='w', encoding='utf-8') as f:
            json.dump(new_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (only if the JSON file
        exists; otherwise, do nothing)"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, mode='r', encoding='utf-8') as f:
                new_dict = json.load(f)
            for key, value in new_dict.items():
                class_name = value["__class__"]
                obj = eval(class_name + "(**value)")
                FileStorage.__objects[key] = obj
        else:
            return
    
    def delete(self, obj=None):
        """Deletes obj from __objects if it’s inside"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()
    
    def close(self):
        """Method for deserializing the JSON file to objects"""
        self.reload()
