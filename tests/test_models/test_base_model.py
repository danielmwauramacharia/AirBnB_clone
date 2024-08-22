#!/usr/bin/python3
"""Module to test the BaseModel Class"""
import unittest
from datetime import datetime
import time
from uuid import uuid4
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test case for the basemodel"""

    def test_initialization(self):
        """Test the __init__ method"""
        model = BaseModel()
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(str(type(model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """Testing the method save in base_model module"""
        test = BaseModel()
        time.sleep(0.5)
        now = datetime.now()
        test.save()
        diff = test.updated_at - now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)

    def test_to_dict(self):
        """Test the to_dict method"""
        dict_inst = BaseModel()
        to_dict = dict_inst.to_dict()
        self.assertIsInstance(to_dict, dict)
        self.assertIn("id", to_dict.keys())
        self.assertIn("created_at", to_dict.keys())
        self.assertIn("updated_at", to_dict.keys())
        self.assertEqual(to_dict['__class__'], type(to_dict).__name__)

    def test_str(self):
        """Testing the string representation of the object"""
        model = BaseModel()
        str_repr = f"[{model.__class__.__name__}] ({model.id}) {
            model.__dict__}"
        self.assertEqual(print(model), str_repr)


if __name__ == "__main__":
    unittest.main()
