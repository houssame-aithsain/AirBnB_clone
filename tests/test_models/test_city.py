#!/usr/bin/python3
""" Test for City class"""

import os
import unittest
from models.engine.file_storage import FileStorage
from models import storage
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Test cases for the `City` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        c1 = City()
        c2 = City(**c1.to_dict())
        c3 = City("hello", "wait", "in")

        k = f"{type(c1).__name__}.{c1.id}"
        self.assertIsInstance(c1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(c3.name, "")

    def test_str(self):
        """Test method for str representation"""
        c1 = City()
        string = f"[{type(c1).__name__}] ({c1.id}) {c1.__dict__}"
        self.assertEqual(c1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        c1 = City()
        old_update = c1.updated_at
        c1.save()
        self.assertNotEqual(c1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        c1 = City()
        self.assertIsInstance(c1.to_dict(), dict)
        self.assertEqual(c1.__class__.__name__, 'City')
