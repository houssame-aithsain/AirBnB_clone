#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Defines the City class."""

from models.base_model import BaseModel


class City(BaseModel):
    """Creates a new city."""
    state_id = ""
    name = ""
