#!/usr/bin/python3
"""
Unittests for FileStorage class
"""
import unittest
import os
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the tests"""
        cls.storage = FileStorage()
        cls.file_path = 'file.json'

    def setUp(self):
        """Reset the storage and file before each test"""
        self.storage.reload()
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test all method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_new(self):
        """Test new method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_save(self):
        """Test save method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists(self.file_path))

    def test_reload(self):
        """Test reload method"""
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(f"BaseModel.{obj.id}", self.storage.all())

    def test_reload_empty_file(self):
        """Test reload method with empty file"""
        open(self.file_path, 'w').close()
        self.storage.reload()
        self.assertEqual(self.storage.all(), {})


if __name__ == '__main__':
    unittest.main()
