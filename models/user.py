#!/usr/bin/python3
"""Module for the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """CLass that inherits from BaseModel
       with public attributes:
       email
       password
       first_name
       last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
