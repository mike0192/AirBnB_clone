#!/usr/bin/python3
"""MOdule for the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Class for representing a user data
       for the AirBnB clone

       with empty string public instance attributes:
        email
        password
        first_name
        last_name
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
