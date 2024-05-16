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

    def get(self, cls, id):
        """Method to retrieve one object"""
        key = "{}.{}".format(cls.__name__, id)
        if key in self.__objects:
            return self.__objects[key]
        return None
    
    def count(self, cls=None):
        """Method to count the number of objects in storage"""
        if cls is not None:
            count = 0
            for key in self.__objects:
                if key.split(".")[0] == cls.__name__:
                    count += 1
            return count
        return len(self.__objects)
    
    def get_all(self, cls=None):
        """Method to retrieve all objects"""
        if cls is not None:
            return [value for key, value in self.__objects.items() if key.split(".")[0] == cls.__name__]
        return self.__objects.values()
    
    def get_all_by(self, cls, attr, value):
        """Method to retrieve all objects by attribute"""
        return [value for value in self.get_all(cls) if getattr(value, attr) == value]
    
    def get_first(self, cls, attr, value):
        """Method to retrieve the first object by attribute"""
        for obj in self.get_all(cls):
            if getattr(obj, attr) == value:
                return obj
        return None
    
    def get_all_by_attr(self, cls, attr, value):
        """Method to retrieve all objects by attribute"""
        return [value for value in self.get_all(cls) if getattr(value, attr) == value]
    
    def get_first_by_attr(self, cls, attr, value):
        """Method to retrieve the first object by attribute"""
        for obj in self.get_all(cls):
            if getattr(obj, attr) == value:
                return obj
        return None
    
    def get_all_by_id(self, cls, id):
        """Method to retrieve all objects by id"""
        return [value for value in self.get_all(cls) if value.id == id]
    
    def get_first_by_id(self, cls, id):
        """Method to retrieve the first object by id"""
        for obj in self.get_all(cls):
            if obj.id == id:
                return obj
        return None
    
    def get_all_by_name(self, cls, name):
        """Method to retrieve all objects by name"""
        return [value for value in self.get_all(cls) if value.name == name]
    
    def get_first_by_name(self, cls, name):
        """Method to retrieve the first object by name"""
        for obj in self.get_all(cls):
            if obj.name == name:
                return obj
        return None
    
    def get_all_by_email(self, cls, email):
        """Method to retrieve all objects by email"""
        return [value for value in self.get_all(cls) if value.email == email]
    
    def get_first_by_email(self, cls, email):
        """Method to retrieve the first object by email"""
        for obj in self.get_all(cls):
            if obj.email == email:
                return obj
        return None
    
    def get_all_by_password(self, cls, password):
        """Method to retrieve all objects by password"""
        return [value for value in self.get_all(cls) if value.password == password]
    
    def get_first_by_password(self, cls, password):
        """Method to retrieve the first object by password"""
        for obj in self.get_all(cls):
            if obj.password == password:
                return obj
        return None
    
    def get_all_by_first_name(self, cls, first_name):
        """Method to retrieve all objects by first_name"""
        return [value for value in self.get_all(cls) if value.first_name == first_name]
    
    def get_first_by_first_name(self, cls, first_name):
        """Method to retrieve the first object by first_name"""
        for obj in self.get_all(cls):
            if obj.first_name == first_name:
                return obj
        return None
    
    def get_all_by_last_name(self, cls, last_name):
        """Method to retrieve all objects by last_name"""
        return [value for value in self.get_all(cls) if value.last_name == last_name]
    
    def get_first_by_last_name(self, cls, last_name):
        """Method to retrieve the first object by last_name"""
        for obj in self.get_all(cls):
            if obj.last_name == last_name:
                return obj
        return None
    
    def get_all_by_city_id(self, cls, city_id):
        """Method to retrieve all objects by city_id"""
        return [value for value in self.get_all(cls) if value.city_id == city_id]
    
    def get_first_by_city_id(self, cls, city_id):
        """Method to retrieve the first object by city_id"""
        for obj in self.get_all(cls):
            if obj.city_id == city_id:
                return obj
        return None
    
    def get_all_by_user_id(self, cls, user_id):
        """Method to retrieve all objects by user_id"""
        return [value for value in self.get_all(cls) if value.user_id == user_id]
    
    def get_first_by_user_id(self, cls, user_id):
        """Method to retrieve the first object by user_id"""
        for obj in self.get_all(cls):
            if obj.user_id == user_id:
                return obj
        return None
    
    def get_all_by_state_id(self, cls, state_id):
        """Method to retrieve all objects by state_id"""
        return [value for value in self.get_all(cls) if value.state_id == state_id]
    
    def get_first_by_state_id(self, cls, state_id):
        """Method to retrieve the first object by state_id"""
        for obj in self.get_all(cls):
            if obj.state_id == state_id:
                return obj
        return None
    
    def get_all_by_amenity_id(self, cls, amenity_id):
        """Method to retrieve all objects by amenity_id"""
        return [value for value in self.get_all(cls) if value.amenity_id == amenity_id]

    def get_first_by_amenity_id(self, cls, amenity_id):
        """Method to retrieve the first object by amenity_id"""
        for obj in self.get_all(cls):
            if obj.amenity_id == amenity_id:
                return obj
        return None

    def get_all_by_place_id(self, cls, place_id):
        """Method to retrieve all objects by place_id"""
        return [value for value in self.get_all(cls) if value.place_id == place_id]

    classes = { "BaseModel": BaseModel }
