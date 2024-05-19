#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

import os
import unittest
from models.engine.file_storage import FileStorage
from models.place import Place
from models import storage
from datetime import datetime


class TestPlace(unittest.TestCase):
    """Test cases for the `Place` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        p1 = Place()
        p2 = Place(**p1.to_dict())
        p3 = Place("hello", "wait", "in")

        k = f"{type(p1).__name__}.{p1.id}"
        self.assertIsInstance(p1.name, str)
        self.assertIn(k, storage.all())
        self.assertEqual(p3.name, "")
        self.assertEqual(p3.city_id, "")
        self.assertEqual(p3.user_id, "")
        self.assertEqual(p3.description, "")
        self.assertEqual(p3.number_rooms, 0)
        self.assertEqual(p3.number_bathrooms, 0)
        self.assertEqual(p3.max_guest, 0)
        self.assertEqual(p3.price_by_night, 0)
        self.assertEqual(p3.latitude, 0.0)
        self.assertEqual(p3.longitude, 0.0)
        self.assertEqual(p3.amenity_ids, [])

    def test_str(self):
        """Test method for str representation"""
        p1 = Place()
        string = f"[{type(p1).__name__}] ({p1.id}) {p1.__dict__}"
        self.assertEqual(p1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        p1 = Place()
        old_update = p1.updated_at
        p1.save()
        self.assertNotEqual(p1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        p1 = Place()
        self.assertIsInstance(p1.to_dict(), dict)
        self.assertEqual(p1.__class__.__name__, 'Place')

    def test_place_instance(self):
        """Test instance of Place"""
        p1 = Place()
        self.assertIsInstance(p1, Place)


if __name__ == '__main__':
    unittest.main()
