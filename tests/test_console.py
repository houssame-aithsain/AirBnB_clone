#!/usr/bin/python3
"""This module defines a base class for all models in the AirBnB project."""

from io import StringIO
import os
import unittest
from unittest.mock import patch
from console import HBNBCommand
from models import storage
import json
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestConsole(unittest.TestCase):
    """Test cases for the console."""
    def setUp(self):
        """Sets up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Cleans up the mock stdin and stdout."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_create_user(self):
        """Test the create command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))

    def test_create_place(self):
        """Test the create command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Place"))

    def test_create_state(self):
        """Test the create command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create State"))

    def test_create_city(self):
        """Test the create command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create City"))

    def test_create_amenity(self):
        """Test the create command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Amenity"))

    def test_create_review(self):
        """Test the create command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Review"))

    def test_show_base_model(self):
        """Test the show command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show BaseModel"))

    def test_show_user(self):
        """Test the show command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show User"))

    def test_show_place(self):
        """Test the show command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show Place"))

    def test_show_state(self):
        """Test the show command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show State"))

    def test_show_city(self):
        """Test the show command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show City"))

    def test_show_amenity(self):
        """Test the show command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show Amenity"))

    def test_show_review(self):
        """Test the show command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show Review"))

    def test_destroy_base_model(self):
        """Test the destroy command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy BaseModel"))

    def test_destroy_user(self):
        """Test the destroy command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy User"))

    def test_destroy_place(self):
        """Test the destroy command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy Place"))

    def test_destroy_state(self):
        """Test the destroy command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy State"))

    def test_destroy_city(self):
        """Test the destroy command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy City"))

    def test_destroy_amenity(self):
        """Test the destroy command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy Amenity"))

    def test_destroy_review(self):
        """Test the destroy command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy Review"))

    def test_all_base_model(self):
        """Test the all command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all BaseModel"))

    def test_all_user(self):
        """Test the all command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all User"))

    def test_all_place(self):
        """Test the all command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all Place"))

    def test_all_state(self):
        """Test the all command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all State"))

    def test_all_city(self):
        """Test the all command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all City"))

    def test_all_amenity(self):
        """Test the all command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all Amenity"))

    def test_all_review(self):
        """Test the all command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all Review"))

    def test_update_base_model(self):
        """Test the update command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update BaseModel"))

    def test_update_user(self):
        """Test the update command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update User"))

    def test_update_place(self):
        """Test the update command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update Place"))

    def test_update_state(self):
        """Test the update command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update State"))

    def test_update_city(self):
        """Test the update command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update City"))

    def test_update_amenity(self):
        """Test the update command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update Amenity"))

    def test_update_review(self):
        """Test the update command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update Review"))

    def test_create(self):
        """Test the create command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create"))

    def test_show(self):
        """Test the show command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("show"))

    def test_destroy(self):
        """Test the destroy command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("destroy"))

    def test_all(self):
        """Test the all command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("all"))

    def test_update(self):
        """Test the update command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("update"))

    def test_emptyline(self):
        """Test the emptyline command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd(""))


class TestUser(unittest.TestCase):
    """Test cases for the `User` class."""
    def setUp(self):
        """Sets up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Cleans up the mock stdin and stdout."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_create_user(self):
        """Test the create command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))

    def test_create_place(self):
        """Test the create command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Place"))

    def test_create_state(self):
        """Test the create command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create State"))

    def test_create_city(self):
        """Test the create command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create City"))

    def test_create_amenity(self):
        """Test the create command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Amenity"))

    def test_create_review(self):
        """Test the create command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Review"))


class BaseModelTestNotation(unittest.TestCase):
    """Test cases for the BaseModel class."""
    def setUp(self):
        """Sets up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Cleans up the mock stdin and stdout."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_create_user(self):
        """Test the create command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))

    def test_create_place(self):
        """Test the create command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Place"))

    def test_create_state(self):
        """Test the create command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create State"))

    def test_create_city(self):
        """Test the create command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create City"))

    def test_create_amenity(self):
        """Test the create command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Amenity"))

    def test_create_review(self):
        """Test the create command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Review"))


class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""
    def setUp(self):
        """Sets up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Cleans up the mock stdin and stdout."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_create_user(self):
        """Test the create command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))

    def test_create_place(self):
        """Test the create command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Place"))

    def test_create_state(self):
        """Test the create command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create State"))

    def test_create_city(self):
        """Test the create command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create City"))

    def test_create_amenity(self):
        """Test the create command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Amenity"))

    def test_create_review(self):
        """Test the create command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Review"))


class TestNotation(unittest.TestCase):
    """Test cases for the User class."""
    def setUp(self):
        """Sets up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Cleans up the mock stdin and stdout."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_create_user(self):
        """Test the create command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))

    def test_create_place(self):
        """Test the create command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Place"))

    def test_create_state(self):
        """Test the create command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create State"))

    def test_create_city(self):
        """Test the create command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create City"))

    def test_create_amenity(self):
        """Test the create command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Amenity"))

    def test_create_review(self):
        """Test the create command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Review"))


class Test_State(unittest.TestCase):
    """Test cases for the State class."""
    def setUp(self):
        """Sets up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Cleans up the mock stdin and stdout."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_create_user(self):
        """Test the create command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))

    def test_create_place(self):
        """Test the create command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Place"))

    def test_create_state(self):
        """Test the create command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create State"))

    def test_create_city(self):
        """Test the create command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create City"))

    def test_create_amenity(self):
        """Test the create command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Amenity"))

    def test_create_review(self):
        """Test the create command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Review"))


class TestCity(unittest.TestCase):
    """Test cases for the City class."""
    def setUp(self):
        """Sets up the mock stdin and stdout."""
        self.console = HBNBCommand()
        self.mock_stdin = patch('sys.stdin', StringIO())
        self.mock_stdout = patch('sys.stdout', StringIO())
        self.mock_stdin.start()
        self.mock_stdout.start()

    def tearDown(self):
        """Cleans up the mock stdin and stdout."""
        self.mock_stdin.stop()
        self.mock_stdout.stop()

    def test_quit(self):
        """Test the quit command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("quit"))

    def test_EOF(self):
        """Test the EOF command."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.console.onecmd("EOF"))

    def test_create_base_model(self):
        """Test the create command with BaseModel."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create BaseModel"))

    def test_create_user(self):
        """Test the create command with User."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create User"))

    def test_create_place(self):
        """Test the create command with Place."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Place"))

    def test_create_state(self):
        """Test the create command with State."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create State"))

    def test_create_city(self):
        """Test the create command with City."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create City"))

    def test_create_amenity(self):
        """Test the create command with Amenity."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Amenity"))

    def test_create_review(self):
        """Test the create command with Review."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertFalse(self.console.onecmd("create Review"))
