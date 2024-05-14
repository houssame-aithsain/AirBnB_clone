#!/usr/bin/python3

''' Import the FileStorage class from the engine module '''

from .engine.file_storage import FileStorage
''' Create a FileStorage instance '''

storage = FileStorage()
storage.reload()
