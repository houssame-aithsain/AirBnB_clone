#!/usr/bin/python3
# this is the test for amenity

import unittest
from models.amenity import Amenity
from models import storage
import os
import inspect
from models.engine.file_storage import FileStorage
import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for the `Amenity` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        a1 = Amenity()
        a2 = Amenity(**a1.to_dict())
        a3 = Amenity("hello", "wait", "in")

        k = f"{type(a1).__name__}.{a1.id}"
        self.assertIsInstance(a1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(a3.name, "")

    def test_str(self):
        """Test method for str representation"""
        a1 = Amenity()
        string = f"[{type(a1).__name__}] ({a1.id}) {a1.__dict__}"
        self.assertEqual(a1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        a1 = Amenity()
        old_update = a1.updated_at
        a1.save()
        self.assertNotEqual(a1.updated_at, old_update)
