#!/usr/bin/python3

"""Module that stores a file attributes for the serialization
   and deserialization process
"""

import json
from models.base_model import BaseModel


class FileStorage:
    """CLass that is going to be a storage engine for
       the other models with private attributes __file_path(str)
       and __objects(dict)
    """
    __file_path = "bruka.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects inside
           the FileStorage engine
        """
        return FileStorage.__objects

    def new(self, obj):
        """Method that Sets in __objects obj with
           key <obj_class_name>.id
        """
        class_name = obj.__class__.__name__
        key = f"{class_name}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Method that Serializes __objects to the JSON file"""

        storage_dict = FileStorage.__objects
        obj_dict = {obj: storage_dict[obj].to_dict() for obj in storage_dict.keys()}
        with open(FileStorage.__file_path, "w") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """Method that deserializes the JSON file __file_path to __objects,
           if it exists, otherwise do nothing
        """
        try:
            with open(FileStorage.__file_path) as file:
                obj_dict = json.load(file)
                for ob in obj_dict.values():
                    class_name = ob["__class__"]
                    del ob["__class__"]
                    self.new(eval(class_name)(**ob))
        except FileNotFoundError:
            return
