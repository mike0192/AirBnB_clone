#!/usr/bin/python3

""" Module for unittesting Amenity model
"""
import os
import models
import unittest
from datetime import datetime
from time import sleep
from models.amenity import Amenity


class Test_amenity_save(unittest.TestCase):
    """Class for Unittesting for testing save
       method of the Amenity class
    """

    @classmethod
    def setUp(self):
        try:
            os.rename("bruka.json", "tmp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("bruka.json")
        except IOError:
            pass
        try:
            os.rename("tmp", "bruka.json")
        except IOError:
            pass

    def test_one_save(self):
        amnt = Amenity()
        sleep(0.05)
        first_updated_at = amnt.updated_at
        amnt.save()
        self.assertLess(first_updated_at, amnt.updated_at)

    def test_two_saves(self):
        amnt = Amenity()
        sleep(0.05)
        first_updated_at = amnt.updated_at
        amnt.save()
        second_updated_at = amnt.updated_at
        self.assertLess(first_updated_at, second_updated_at)
        sleep(0.05)
        amnt.save()
        self.assertLess(second_updated_at, amnt.updated_at)

    def test_save_with_arg(self):
        amnt = Amenity()
        with self.assertRaises(TypeError):
            amnt.save(None)

    def test_save_updates_file(self):
        amnt = Amenity()
        amnt.save()
        amntid = "Amenity." + amnt.id
        with open("bruka.json", "r") as f:
            self.assertIn(amntid, f.read())


class Test_amenity_to_dict(unittest.TestCase):
    """Class for Unittesting for testing to_dict
       method of the Amenity class
    """

    def test_to_dict_type(self):
        self.assertTrue(dict, type(Amenity().to_dict()))

    def test_to_dict_contains_correct_keys(self):
        amnt = Amenity()
        self.assertIn("id", amnt.to_dict())
        self.assertIn("created_at", amnt.to_dict())
        self.assertIn("updated_at", amnt.to_dict())
        self.assertIn("__class__", amnt.to_dict())

    def test_to_dict_contains_added_attributes(self):
        amnt = Amenity()
        amnt.middle_namnte = "Yabker"
        amnt.my_number = 98
        self.assertEqual("Yabker", amnt.middle_namnte)
        self.assertIn("my_number", amnt.to_dict())

    def test_to_dict_datetime_attributes_are_strs(self):
        amnt = Amenity()
        amnt_dict = amnt.to_dict()
        self.assertEqual(str, type(amnt_dict["id"]))
        self.assertEqual(str, type(amnt_dict["created_at"]))
        self.assertEqual(str, type(amnt_dict["updated_at"]))

    def test_to_dict_output(self):
        date = datetime.today()
        amnt = Amenity()
        amnt.id = "123456"
        amnt.created_at = amnt.updated_at = date
        tdict = {
            'id': '123456',
            '__class__': 'Amenity',
            'created_at': date.isoformat(),
            'updated_at': date.isoformat(),
        }
        self.assertDictEqual(amnt.to_dict(), tdict)

    def test_contrast_to_dict_dunder_dict(self):
        amnt = Amenity()
        self.assertNotEqual(amnt.to_dict(), amnt.__dict__)

    def test_to_dict_with_arg(self):
        amnt = Amenity()
        with self.assertRaises(TypeError):
            amnt.to_dict(None)


class Test_amenity_init(unittest.TestCase):
    """Class for unittesting for testing instantiation of
       the Amenity class
    """

    def test_no_args_init(self):
        self.assertEqual(Amenity, type(Amenity()))

    def test_new_instance_stored_in_objects(self):
        self.assertIn(Amenity(), models.storage.all().values())

    def test_id_is_public_string(self):
        self.assertEqual(str, type(Amenity().id))

    def test_created_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at_is_public_datetime(self):
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_two_amntenities_unique_ids(self):
        amnt1 = Amenity()
        amnt2 = Amenity()
        self.assertNotEqual(amnt1.id, amnt2.id)

    def test_two_amntenities_different_created_at(self):
        amnt1 = Amenity()
        sleep(0.05)
        amnt2 = Amenity()
        self.assertLess(amnt1.created_at, amnt2.created_at)

    def test_two_amntenities_different_updated_at(self):
        amnt1 = Amenity()
        sleep(0.05)
        amnt2 = Amenity()
        self.assertLess(amnt1.updated_at, amnt2.updated_at)

    def test_str_representation(self):
        date = datetime.today()
        date_repr = repr(date)
        amnt = Amenity()
        amnt.id = "123456"
        amnt.created_at = amnt.updated_at = date
        amntstr = amnt.__str__()
        self.assertIn("[Amenity] (123456)", amntstr)
        self.assertIn("'id': '123456'", amntstr)
        self.assertIn("'created_at': " + date_repr, amntstr)
        self.assertIn("'updated_at': " + date_repr, amntstr)

    def test_args_unused(self):
        amnt = Amenity(None)
        self.assertNotIn(None, amnt.__dict__.values())

    def test_instantiation_with_kwargs(self):
        """instantiation with kwargs test method"""
        date = datetime.today()
        date_iso = date.isoformat()
        amnt = Amenity(id="345", created_at=date_iso, updated_at=date_iso)
        self.assertEqual(amnt.id, "345")
        self.assertEqual(amnt.created_at, date)
        self.assertEqual(amnt.updated_at, date)

    def test_instantiation_with_None_kwargs(self):
        with self.assertRaises(TypeError):
            Amenity(id=None, created_at=None, updated_at=None)


if __name__ == "__main__":
    unittest.main()
