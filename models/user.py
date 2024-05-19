#!usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines the User class."""

from models.base_model import BaseModel


class User(BaseModel):
    """Creates a new user"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
