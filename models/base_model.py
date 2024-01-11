#!/usr/bin/python3

""" Base model for all the other classes to inherit"""

from datetime import datetime
import uuid


class BaseModel:
    """ BaseModel class that with instance attributes and
        instance methods
    """

    def __init__(self, *args, **kwargs):
        """Magic function for initializing attributes id, created_at,
           updated_at

           *args: Tuple containg all the arguments but it's
                 not used here
           **kwargs: is a dictionary with key/value attributes
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        time_format = "%Y-%m-%dT%H:%M:%S.%f"

        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                else:
                    self.__dict__[key] = value

    def __str__(self):
        """ dunder method that returns the human readable
            method of string of an object
        """
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """ Method that updates the public instance attributes
            with the current date time
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ Method that returns the dictionary containing all keys/values
            of the __dict__
        """
        base = self.__dict__.copy()

        base['__class__'] = self.__class__.__name__
        base['created_at'] = self.created_at.isoformat()
        base['updated_at'] = self.updated_at.isoformat()

        return base
