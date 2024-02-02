
import unittest
from unittest.mock import patch
from dataclasses import is_dataclass
from __seedwork.domain.value_objects import UniqueEntityId
from __seedwork.domain.exceptions import InvalidUuidException
import uuid


class TestUniqueEntityIdUnit(unittest.TestCase):

    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))

    def test_throw_exception_when_uuid_is_invalid(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        )as mock_validate:
            with self.assertRaises(InvalidUuidException) as assert_error:
                UniqueEntityId('fake id')
            mock_validate.assert_called_once()
            self.assertEqual(
                assert_error.exception.args[0], 'ID must be a valid UUID')

    def test_accept_uuid_passed_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        )as mock_validate:
            value_object = UniqueEntityId(
                'fb00e814-c08a-4a57-a981-8f34229eae17')
            mock_validate.assert_called_once()
            self.assertEqual(
                value_object.id, 'fb00e814-c08a-4a57-a981-8f34229eae17')

            uuid_value = uuid.uuid4()
            value_object = UniqueEntityId(uuid_value)
            self.assertEqual(
                value_object.id, str(uuid_value))

    def test_generate_id_when_no_passed_id_in_constructor(self):
        with patch.object(
            UniqueEntityId,
            '_UniqueEntityId__validate',
            autospec=True,
            side_effect=UniqueEntityId._UniqueEntityId__validate
        )as mock_validate:
            value_object = UniqueEntityId()
            uuid.UUID(value_object.id)
            mock_validate.assert_called_once()
