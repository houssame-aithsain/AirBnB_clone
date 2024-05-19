#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

import uuid
from datetime import datetime
import models


class BaseModel:
    """A base class for all models in the AirBnB project."""

    def __init__(self, *args, **kwargs):
        """Initialize a new `BaseModel`."""
        if kwargs:
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key,
                            datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f'))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """Return a string representation of the `BaseModel`."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Update the `updated_at` attribute and save the instance."""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return a dictionary representation of the `BaseModel`."""
        model_dict = self.__dict__.copy()
        model_dict['__class__'] = self.__class__.__name__
        model_dict['created_at'] = self.created_at.isoformat()
        model_dict['updated_at'] = self.updated_at.isoformat()
        return model_dict
