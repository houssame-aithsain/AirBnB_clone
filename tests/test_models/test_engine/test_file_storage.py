#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestBaseModel(unittest.TestCase):
    """Test cases for the `BaseModel` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        b1 = BaseModel()
        b2 = BaseModel(**b1.to_dict())
        b3 = BaseModel("hello", "wait", "in")

    def test_str(self):
        """Test method for str representation"""
        b1 = BaseModel()
        string = f"[{type(b1).__name__}] ({b1.id}) {b1.__dict__}"
        self.assertEqual(b1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        b1 = BaseModel()
        old_update = b1.updated_at
        b1.save()
        self.assertNotEqual(b1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        b1 = BaseModel()
        self.assertIsInstance(b1.to_dict(), dict)
        self.assertEqual(b1.__class__.__name__, 'BaseModel')

    def test_id(self):
        """Test method for id"""
        b1 = BaseModel()
        self.assertIsInstance(b1.id, str)

    def test_save(self):
        """Test method for save"""
        b1 = BaseModel()
        old_update = b1.updated_at
        b1.save()
        self.assertNotEqual(b1.updated_at, old_update)

    def test_to_dict(self):
        """Test method for to_dict"""
        b1 = BaseModel()
        self.assertIsInstance(b1.to_dict(), dict)
        self.assertEqual(b1.__class__.__name__, 'BaseModel')

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)

    def test_instance(self):
        """Test instance of BaseModel"""
        b1 = BaseModel()
        self.assertIsInstance(b1, BaseModel)
