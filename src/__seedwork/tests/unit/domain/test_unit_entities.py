import unittest
from __seedwork.domain.entities import Entity
from dataclasses import is_dataclass , dataclass
from abc import ABC
from src.__seedwork.domain.value_objects import UniqueEntityId


@dataclass(frozen=True,kw_only=True)
class StubEntity(Entity):
    prop1: str
    prop2: str

class TestEntityUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Entity))
    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(Entity(), ABC)

    def test_set_unique_entity_id_and_prop(self):
        entity = StubEntity(prop1='prop1',prop2='prop2')
        self.assertEqual(entity.prop1, 'prop1')
        self.assertEqual(entity.prop2, 'prop2')
        self.assertIsInstance(entity.unique_entity_id, UniqueEntityId)
        self.assertEqual(entity.unique_entity_id.id, entity.id)
    
    def test_account_a_valid_uuid(self):
        entity = StubEntity(unique_entity_id="2506e4ca-4cda-4e2e-ae87-763208d223c3",prop1='prop1',prop2='prop2')
        self.assertEqual(entity.unique_entity_id, '2506e4ca-4cda-4e2e-ae87-763208d223c3')

    def test_metod_to_dict(self):
        entity = StubEntity(unique_entity_id="2506e4ca-4cda-4e2e-ae87-763208d223c3",prop1='prop1',prop2='prop2')
        self.assertDictEqual(entity.to_dict(), {'id':'2506e4ca-4cda-4e2e-ae87-763208d223c3','prop1': 'prop1', 'prop2': 'prop2'})

