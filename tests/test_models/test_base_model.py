"""Module to test the BaseModel Class"""
import unittest
from datetime import datetime
import time
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """Test case for the basemodel"""

    def test_save(self):
        """Testing the method save in base_model module"""
        test = BaseModel()
        time.sleep(0.5)
        now = datetime.now()
        test.save()
        diff = test.updated_at - now
        self.assertTrue(abs(diff.total_seconds()) < 0.01)


if __name__ == "__main__":
    unittest.main()
