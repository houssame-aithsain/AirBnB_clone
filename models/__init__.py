#!/usr/bin/python3
"""
This module initializes the models package.
"""

from models.engine import file_storage


"""Create a FileStorage instance"""
storage = file_storage.FileStorage()
storage.reload()
