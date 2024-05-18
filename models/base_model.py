#!/usr/bin/python3
"""This module contains the BaseModel class for the AirBnB project."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """This class defines all common attributes/methods for other classes."""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel."""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the BaseModel."""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
    
    def save(self):
        """Update the updated_at attribute with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()
    
    def to_dict(self):
        """Return a dictionary representation of the BaseModel."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
    
    def delete(self):
        """Delete the current instance from the storage."""
        models.storage.delete(self)
    
    def __repr__(self):
        """Return a string representation of the BaseModel."""
        return self.__str__()
    
    def __eq__(self, other):
        """Check if two instances are equal."""
        return self.__dict__ == other.__dict__ if other else False
    
    def __ne__(self, other):
        """Check if two instances are not equal."""
        return not self.__eq__(other)
    
    def __lt__(self, other):
        """Check if the current instance is less than another instance."""
        return self.created_at < other.created_at
