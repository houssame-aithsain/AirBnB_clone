#!/usr/bin/python3
# user.py module for the HBNB project.

from models.base_model import BaseModel


class User(BaseModel):
    """A user class that inherits from BaseModel."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialize a new User."""
        super().__init__(*args, **kwargs)
    
    def __str__(self):
        """Return a human-readable string representation of a User."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
    
    def to_dict(self):
        """Return a dictionary representation of a User."""
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
    
    @property
    def email(self):
        """Get the email attribute."""
        return self.email
    
    @property
    def password(self):
        """Get the password attribute."""
        return self.password
    
    @property
    def first_name(self):
        """Get the first_name attribute."""
        return self.first_name
    
    @property
    def last_name(self):
        """Get the last_name attribute."""
        return self.last_name
    
    @email.setter
    def email(self, value):
        """Set the email attribute."""
        self.email = value

    @password.setter
    def password(self, value):
        """Set the password attribute."""
        self.password = value

    @first_name.setter
    def first_name(self, value):
        """Set the first_name attribute."""
        self.first_name = value

    @last_name.setter
    def last_name(self, value):
        """Set the last_name attribute."""
        self.last_name = value

    def __setattr__(self, name, value):
        """Set an attribute of a User."""
        if name == "email":
            self.email = value
        elif name == "password":
            self.password = value
        elif name == "first_name":
            self.first_name = value
        elif name == "last_name":
            self.last_name = value
        else:
            super().__setattr__(name, value)
