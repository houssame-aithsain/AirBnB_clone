#!/usr/bin/python3
"""
Module: __init__.py
"""
from models.engine import file_storage


"""Create a FileStorage instance to manage the storage of the application"""
storage = file_storage.FileStorage()
storage.reload()
