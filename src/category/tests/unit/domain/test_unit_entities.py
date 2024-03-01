from datetime import datetime
import unittest
from dataclasses import is_dataclass, FrozenInstanceError
from category.domain.entities import Category


class TestCategory(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))

    def test_constructor_default(self):
        category = Category(name="Movie")
        self.assertEqual(category.name, "Movie")
        self.assertIsNone(category.description)
        self.assertTrue(category.is_activate)
        self.assertIsInstance(category.created_at, datetime)

    def test_contructor_with_all_params(self):
        created_at = datetime.now()
        category = Category(
            name="Movie",
            description="descrição",
            is_activate=True,
            created_at=created_at,
        )
        self.assertEqual(category.name, "Movie")
        self.assertEqual(category.description, "descrição")
        self.assertTrue(category.is_activate)
        self.assertEqual(category.created_at, created_at)

    def test_if_created_at_is_generated_in_constructor(self):
        category1 = Category(name="Movie1")
        category2 = Category(name="Movie2")
        self.assertNotEqual(
            category1.created_at.timestamp(), category2.created_at.timestamp()
        )

    def test_is_imutable(self):
        with self.assertRaises(FrozenInstanceError):
            category = Category(name="Movie")
            category.name = "Fake Name"

    def test_method_update(self):
        category = Category(name="name", description="description")
        category.update(name="new name", description="new description")
        self.assertEqual(category.name, "new name")
        self.assertEqual(category.description, "new description")

    def test_method_desactivate(self):
        category = Category(name="name", description="descriptioi")
        category.deactivate()
        self.assertFalse(category.is_activate)

    def test_method_activate(self):
        category = Category(name="name", description="descriptioi", is_activate=False)
        category.activate()
        self.assertTrue(category.is_activate)
