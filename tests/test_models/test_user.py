#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.user import User
from models import storage
from datetime import datetime


class TestUser(unittest.TestCase):
    """Test cases for the `User` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        u1 = User()
        u2 = User(**u1.to_dict())
        u3 = User("hello", "wait", "in")

        k = f"{type(u1).__name__}.{u1.id}"
        self.assertIsInstance(u1.email, str)
        self.assertIn(k, storage.all())
        self.assertEqual(u3.email, "")
        self.assertEqual(u3.password, "")
        self.assertEqual(u3.first_name, "")
        self.assertEqual(u3.last_name, "")

    def test_str(self):
        """Test method for str representation"""
        u1 = User()
        string = f"[{type(u1).__name__}] ({u1.id}) {u1.__dict__}"
        self.assertEqual(u1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        u1 = User()
        old_update = u1.updated_at
        u1.save()
        self.assertNotEqual(u1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        u1 = User()
        self.assertIsInstance(u1.to_dict(), dict)
        self.assertEqual(u1.__class__.__name__, 'User')
    
    def test_email(self):
        """Test method for email"""
        u1 = User()
        self.assertIsInstance(u1.email, str)

    def test_password(self):
        """Test method for password"""
        u1 = User()
        self.assertIsInstance(u1.password, str)
    
    def test_first_name(self):
        """Test method for first_name"""
        u1 = User()
        self.assertIsInstance(u1.first_name, str)


if __name__ == "__main__":
    unittest.main()
