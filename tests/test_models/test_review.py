#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

import os
import unittest
from models.review import Review
from models import storage
from datetime import datetime
from models.engine.file_storage import FileStorage


class TestReview(unittest.TestCase):
    """Test cases for the `Review` class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_params(self):
        """Test method for class attributes"""

        r1 = Review()
        r2 = Review(**r1.to_dict())
        r3 = Review("hello", "wait", "in")

        k = f"{type(r1).__name__}.{r1.id}"
        self.assertIsInstance(r1.text, str)
        self.assertIn(k, storage.all())
        self.assertEqual(r3.text, "")
        self.assertEqual(r3.place_id, "")
        self.assertEqual(r3.user_id, "")

    def test_str(self):
        """Test method for str representation"""
        r1 = Review()
        string = f"[{type(r1).__name__}] ({r1.id}) {r1.__dict__}"
        self.assertEqual(r1.__str__(), string)

    def test_save(self):
        """Test method for save"""
        r1 = Review()
        old_update = r1.updated_at
        r1.save()
        self.assertNotEqual(r1.updated_at, old_update)

    def test_todict(self):
        """Test method for dict"""
        r1 = Review()
        self.assertIsInstance(r1.to_dict(), dict)
        self.assertEqual(r1.__class__.__name__, 'Review')

    def test_text(self):
        """Test method for text"""
        r1 = Review()
        self.assertIsInstance(r1.text, str)
        self.assertEqual(r1.text, "")

    def test_place_id(self):
        """Test method for place_id"""
        r1 = Review()
        self.assertIsInstance(r1.place_id, str)
        self.assertEqual(r1.place_id, "")

    def test_user_id(self):
        """Test method for user_id"""
        r1 = Review()
        self.assertIsInstance(r1.user_id, str)
        self.assertEqual(r1.user_id, "")

    def test_review_instance(self):
        """Test instance of Review"""
        r1 = Review()
        self.assertIsInstance(r1, Review)
