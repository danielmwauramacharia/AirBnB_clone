#!/usr/bin/python3
"""module: File storage test"""
import unittest
import os
import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel


class TestFileStorageInstantiation(unittest.TestCase):
    """Test initialization of storage"""

    def test_FileStorage_instantiation_no_args(self):
        """test creation of a storage instance with no arguments"""
        self.assertEqual(type(FileStorage), FileStorage)

    def test_FileStorage_instantiation_args(self):
        """Create a File storage with an argument, an error shoul be raised"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def storage_initializes(self):
        """Check if storage variable is instance of Filestorage"""
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage(unittest.TestCase):
    """Tests the file storage in the json file"""

    def setUp(self) -> None:
        """create a temporary json file"""
        self.test_file = "test_file.json"

    def tearDown(self) -> None:
        """Remove the temporary file after test"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_all_storage_return_dictionary(self):
        """Test id all method returns a dict"""
        self.assertEqual(dict, type(models.storage.all()))

    def test_new(self):
        """Test the new method by creating an object"""
        model = BaseModel()
        models.storage.new(model)
        self.assertIn(f"BaseModel.{model.id}", models.storage.all())

    def test_new_with_args(self):
        """
        Test creating a new object with additional arguments
        should raise TypeError
        """
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel())

    def test_new_with_None(self):
        """
        creating an object with none
        Raises an Attribute Error
        """
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_and_reload(self):
        """Test loading object to a file and Reloading it"""
        model = BaseModel()
        model1 = BaseModel()
        models.storage.new(model)
        models.storage.new(model1)
        models.storage.save()

        # create a storage instance to emulate reloading
        new_storage = FileStorage()
        new_storage.reload()

        # check if the reloaded object match the original objects
        self.assertTrue(new_storage.all().get(
            f"Basemodel.{model.id}") is not None)
        self.assertTrue(new_storage.all().get(
            f"Basemodel.{model1.id}") is not None)

    def test_save_to_file(self):
        """Test saving object to a file and check if the file is created"""
        model = BaseModel()
        models.storage.new(model)
        models.storage.save()
        self.assertTrue(os.path.exists(models.storage._FileStorage__file_path))

    def test_reload_empy_file(self):
        """Reload when the file is empty or non existent"""
        with self.assertRaises(TypeError):
            models.storage.reload()


if __name__ == '__main__':
    unittest.main()
