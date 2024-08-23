#!/usr/bin/python3
"""Module to test the BaseModel Class"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test case for the basemodel"""

    def test_init(self):
        """Test the __init__ method of BaseModel"""
        model = BaseModel()
        self.assertIsNotNone(model.id)
        self.assertIsNotNone(model.created_at)
        self.assertIsNotNone(model.updated_at)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertEqual(str(type(model)),
                         "<class 'models.base_model.BaseModel'>")

    def test_save(self):
        """Testing the method save of the BaseModel"""
        model = BaseModel()
        creation_time = model.created_at
        model.save()
        update_time = model.updated_at
        self.assertNotEqual(creation_time, update_time)

    def test_to_dict(self):
        """Test the to_dict method"""
        model = BaseModel()
        to_dict = model.to_dict()
        self.assertIsInstance(to_dict, dict)
        self.assertIn("id", to_dict.keys())
        self.assertIn("created_at", to_dict.keys())
        self.assertIn("updated_at", to_dict.keys())
        self.assertEqual(to_dict['__class__'], model.__class__.__name__)
        self.assertEqual(to_dict["id"], model.id)
        self.assertEqual(to_dict["created_at"], model.created_at.isoformat())
        self.assertEqual(to_dict["updated_at"], model.updated_at.isoformat())

    def test_str(self):
        """Testing the string representation of the object"""
        model = BaseModel()
        self.assertTrue(str(model).startswith('[BaseModel]'))
        self.assertIn(model.id, str(model))
        self.assertIn(str(model.__dict__), str(model))
        str_repr = f"[{model.__class__.__name__}] ({model.id}) {
            model.__dict__}"
        self.assertEqual(str(model), str_repr)


if __name__ == "__main__":
    unittest.main()
