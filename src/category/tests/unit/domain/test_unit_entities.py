from datetime import datetime
import unittest
from dataclasses import is_dataclass, FrozenInstanceError
from category.domain.entities import Category


class TestCategory(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor(self):
        category = Category(name='Movie')
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, None)
        self.assertEqual(category.is_activate, True)
        self.assertIsInstance(category.created_at, datetime)

        created_at = datetime.now()
        category = Category(
            name='Movie',
            description='descrição',
            is_activate=True,
            created_at=created_at)
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'descrição')
        self.assertEqual(category.is_activate, True)
        self.assertEqual(category.created_at, created_at)

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category(name='Movie1')
        category2 = Category(name='Movie2')
        self.assertNotEqual(category1.created_at.timestamp(),
                            category2.created_at.timestamp())

    def test_is_imutable(self):
        with self.assertRaises(FrozenInstanceError):
            category = Category(name='Movie')
            category.name = 'Fake Name'
