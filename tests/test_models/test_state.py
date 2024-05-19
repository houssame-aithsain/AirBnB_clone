#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.state import State
from models import storage
from datetime import datetime


class TestState(unittest.TestCase):
    """Test cases for the `State` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        s1 = State()
        s2 = State(**s1.to_dict())
        s3 = State("hello", "wait", "in")

        k = f"{type(s1).__name__}.{s1.id}"
        self.assertIsInstance(s1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(s3.name, "")

    def test_str(self):
        """Test method for str representation"""
        s1 = State()
        string = f"[{type(s1).__name__}] ({s1.id}) {s1.__dict__}"
        self.assertEqual(s1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        s1 = State()
        old_update = s1.updated_at
        s1.save()
        self.assertNotEqual(s1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        s1 = State()
        self.assertIsInstance(s1.to_dict(), dict)
        self.assertEqual(s1.__class__.__name__, 'State')

    def test_name(self):
        """Test method for name"""
        s1 = State()
        self.assertIsInstance(s1.name, str)

    def test_name(self):
        """Test method for name"""
        s1 = State()
        self.assertIsInstance(s1.name, str)

    def test_name(self):
        """Test method for name"""
        s1 = State()
        self.assertIsInstance(s1.name, str)

    def test_name(self):
        """Test method for name"""
        s1 = State()
        self.assertIsInstance(s1.name, str)


if __name__ == "__main__":
    unittest.main()
