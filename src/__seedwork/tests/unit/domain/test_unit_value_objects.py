from dataclasses import dataclass
import unittest
from unittest.mock import patch
from dataclasses import is_dataclass, FrozenInstanceError
from __seedwork.domain.value_objects import UniqueEntityId
from __seedwork.domain.exceptions import InvalidUuidException
from __seedwork.domain.value_objects import ValueObject
import uuid
from abc import ABC


@dataclass(frozen=True)
class StubOnProp(ValueObject):
    prop: str


@dataclass(frozen=True)
class StubTwoProps(ValueObject):
    prop1: str
    prop2: str


class TestValueObjectUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(ValueObject))

    def test_if_is_a_abstract_class(self):
        self.assertIsInstance(ValueObject(), ABC)

    def test_if_is_prop(self):
        vo1 = StubOnProp("prop")
        self.assertEqual(vo1.prop, "prop")
        vo2 = StubTwoProps("prop1", "prop2")
        self.assertEqual(vo2.prop1, "prop1")

    def test_convert_to_string(self):
        vo1 = StubOnProp("prop")
        self.assertEqual(str(vo1), "prop")
        vo2 = StubTwoProps("prop1", "prop2")
        self.assertEqual(str(vo2), '{"prop1": "prop1", "prop2": "prop2"}')

    def test_is_imutable(self):
        with self.assertRaises(FrozenInstanceError):
            vo = StubOnProp("prop")
            vo.prop = "fake prop"


class TestUniqueEntityIdUnit(unittest.TestCase):
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,
        ) as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId("fake id")
            mock_validate.assert_called_once()
            self.assertEqual(assert_error.exception.args[0], "ID must be a valid UUID")

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,
        ) as mock_validate:
            value_object = UniqueEntityId("fb00e814-c08a-4a57-a981-8f34229eae17")
            mock_validate.assert_called_once()
            self.assertEqual(value_object.id, "fb00e814-c08a-4a57-a981-8f34229eae17")

            uuid_value = uuid.uuid4()
            value_object = UniqueEntityId(uuid_value)
            self.assertEqual(value_object.id, str(uuid_value))

    def test_generate_id_when_no_passed_id_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            "_UniqueEntityId__validate",
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate,
        ) as mock_validate:
            value_object = UniqueEntityId()
            uuid.UUID(value_object.id)
            mock_validate.assert_called_once()

    def test_is_imutable(self):
        with self.assertRaises(FrozenInstanceError):
            value_object = UniqueEntityId()
            value_object.id = "fake id"
