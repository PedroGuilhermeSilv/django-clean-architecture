import unittest
from datetime import datetime
from category.domain.entities import Category

class TestCategory(unittest.TestCase):
    def test_category(self):
        category = Category(name="Category 1", description="Description 1", is_activate=True, created_at=datetime.now())
        self.assertEqual(category.name, "Category 1")
        self.assertEqual(category.description, "Description 1")
        self.assertEqual(category.is_activate, True)
        self.assertIsInstance(category.created_at, datetime)