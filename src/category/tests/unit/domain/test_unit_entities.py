from datetime import datetime
import unittest
from category.domain.entities import Category

class TestCategory(unittest.TestCase):
    def test_constructor(self):
        category = Category(name='Movie',description='descrição', is_activate=True, created_at=datetime.now())
        self.assertEqual(category.name,'Movie')
        self.assertEqual(category.description,'descrição')
        self.assertEqual(category.is_activate, True)
        self.assertIsInstance(category.created_at, datetime)