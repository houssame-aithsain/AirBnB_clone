#!/usr/bin/python3
"""This module defines a class BaseModel that defines all
common attributes/methods for other classes."""

import models
from datetime import datetime
import uuid


class BaseModel:
    """BaseModel class for all classes in the AirBnB clone project."""

    def __str__(self):
        """Return a string representation of the BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs.keys():
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs.keys():
                self.created_at = datetime.today()
            if "updated_at" not in kwargs.keys():
                self.updated_at = datetime.today()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def to_dict(self):
        """to_dic returns a dictionary containing all
        keys/values of __dict__."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict

    def save(self):
        """save method updates the public instance
        attribute updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()
