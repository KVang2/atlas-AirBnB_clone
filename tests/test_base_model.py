"""Test module for models in the application"""

import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime
import os

class TestBaseModel(unittest.TestCase):
    """Test class for the BaseModel class"""

    def setUp(self):
        """Set up method to create an instance of BaseModel for testing"""
        self.model = BaseModel()

    def test_save_method_updates_updated_at(self):
        """Test if the save method updates the 'updated_at' attribute"""
        original_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(original_updated_at, self.model.updated_at)

    def test_to_dict_method_returns_dictionary(self):
        """Test if the to_dict method returns a dictionary with expected keys"""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)

    def test_id_attribute_is_string(self):
        """Test if the 'id' attribute is a string"""
        self.assertIsInstance(self.model.id, str)

    def test_created_at_attribute_is_datetime(self):
        """Test if the 'created_at' attribute is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_str_method_returns_expected_output(self):
        """Test if the __str__ method returns the expected string representation"""
        expected_output = "[BaseModel] ({}) {}".format(self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_output)

    def test_base_model_init_with_args_kwargs(self):
        """Test if BaseModel can be initialized with arguments and keyword arguments"""
        model = BaseModel(id="123", created_at="2022-01-01T00:00:00.000000", updated_at="2022-01-01T00:00:00.000000")
        self.assertEqual(model.id, "123")
        self.assertEqual(model.created_at.year, 2022)
        self.assertEqual(model.updated_at.year, 2022)

    def test_base_model_save_updates_updated_at(self):
        """Test if the save method updates the 'updated_at' attribute"""
        model = BaseModel()
        original_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(original_updated_at, model.updated_at)

class TestFileStorage(unittest.TestCase):
    """Test class for the FileStorage class"""

    def setUp(self):
        """Set up method to create an instance of FileStorage for testing"""
        self.storage = FileStorage()

    def tearDown(self):
        """Tear down method to clean up test files created during testing"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
        except FileNotFoundError:
            pass

    def test_file_path_attribute_exists(self):
        """Test if the '_file_path' attribute exists in FileStorage"""
        self.assertTrue(hasattr(self.storage, '_FileStorage__file_path'))

    def test_objects_attribute_exists(self):
        """Test if the '_objects' attribute exists in FileStorage"""
        self.assertTrue(hasattr(self.storage, '_FileStorage__objects'))

    def test_all_method_returns_dictionary(self):
        """Test if the all method returns a dictionary"""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_to_objects(self):
        """Test if the new method adds an object to the '_objects' attribute"""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(type(model).__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_save_method_saves_to_file(self):
        """Test if the save method saves the data to the file"""
        model = BaseModel()
        key = "{}.{}".format(type(model).__name__, model.id)
        self.storage.new(model)
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage._FileStorage__file_path))
        with open(self.storage._FileStorage__file_path, 'r') as file:
            content = file.read()
            self.assertIn(key, content)

    def test_reload_method_loads_from_file(self):
        """Test if the reload method loads data from the file"""
        model = BaseModel()
        key = "{}.{}".format(type(model).__name__, model.id)
        self.storage.new(model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        self.assertIn(key, new_storage.all())

class TestState(unittest.TestCase):
    """Test class for the State class"""

    def test_state_instance(self):
        """Test if an instance of State can be created"""
        state = State()
        self.assertIsInstance(state, State)

class TestCity(unittest.TestCase):
    """Test class for the City class"""

    def test_city_instance(self):
        """Test if an instance of City can be created"""
        city = City()
        self.assertIsInstance(city, City)

class TestAmenity(unittest.TestCase):
    """Test class for the Amenity class"""

    def test_amenity_instance(self):
        """Test if an instance of Amenity can be created"""
        amenity = Amenity()
        self.assertIsInstance(amenity, Amenity)

class TestPlace(unittest.TestCase):
    """Test class for the Place class"""

    def test_place_instance(self):
        """Test if an instance of Place can be created"""
        place = Place()
        self.assertIsInstance(place, Place)

class TestReview(unittest.TestCase):
    """Test class for the Review class"""

    def test_review_instance(self):
        """Test if an instance of Review can be created"""
        review = Review()
        self.assertIsInstance(review, Review)

if __name__ ==

