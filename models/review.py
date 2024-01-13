#!/usr/bin/python3
"""Module for the Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """CLass review for collecting user reviews
       for the AirBnB clone

       with public instance attributes:
       public_id
       user_id
       text
    """

    place_id = ""
    user_id = ""
    text = ""
