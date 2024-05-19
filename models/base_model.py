#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class for all models in the AirBnB project."""

    def to_dict(self):
        """Get a dictionary representation of a BaseModel."""
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        return new_dict

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
            if "created_at" not in kwargs:
                self.created_at = datetime.today()
            if "updated_at" not in kwargs:
                self.updated_at = datetime.today()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
            models.storage.new(self)

    def __str__(self):
        """Get a string representation of a BaseModel."""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Update the updated_at attribute and save the instance
        to the storage."""
        self.updated_at = datetime.today()
        models.storage.save()
