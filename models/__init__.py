#!/usr/bin/python3

"""Magic method for the initialization of
   of instances of the models package
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
