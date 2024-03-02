import unittest
from parameterized import parameterized

from __seedwork.domain.validators import ValidatorRules


class TestValidorRules(unittest.TestCase):
    def test_values_method(self):
        validator = ValidatorRules.values("value", "prop")
        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, "value")
        self.assertEqual(validator.prop, "prop")

    @parameterized.expand(
        [
            (None, "prop"),
            ("", "prop"),
        ]
    )
    def test_required_rule(self, value, prop):
        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value, prop).required()

        self.assertEqual("prop is required", str(assert_error.exception))

    @parameterized.expand(
        [
            (1, "prop"),
            (True, "prop"),
            (False, "prop"),
            ([], "prop"),
            ({}, "prop"),
        ]
    )
    def test_string_rule_incorrect(self, value, prop):
        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value=value, prop=prop).string()

        self.assertEqual(f"{prop} must be a string", str(assert_error.exception))

    @parameterized.expand([(None, "prop"), ("", "prop"), ("test", "prop")])
    def test_string_rule_correct(self, value, prop):
        self.assertIsInstance(
            ValidatorRules.values(value=value, prop=prop).string(), ValidatorRules
        )

    @parameterized.expand(
        [
            ("t" * 5, "prop"),
        ]
    )
    def test_max_length_rule_incorrect(self, value, prop):
        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value=value, prop=prop).max_length(4)

        self.assertEqual(
            f"{prop} must be less than 4 characters", str(assert_error.exception)
        )

    @parameterized.expand(
        [
            (None, "prop"),
            ("t" * 4, "prop"),
        ]
    )
    def test_max_length_rule_correct(self, value, prop):
        self.assertIsInstance(
            ValidatorRules.values(value=value, prop=prop).max_length(4), ValidatorRules
        )

    @parameterized.expand(
        [
            ("", "prop"),
            ("t", "prop"),
            ({}, "prop"),
        ]
    )
    def test_boolean_rule_incorrect(self, value, prop):
        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value=value, prop=prop).boolean()

        self.assertEqual(f"{prop} must be a boolean", str(assert_error.exception))

    @parameterized.expand(
        [
            (None, "prop"),
            (True, "prop"),
            (False, "prop"),
        ]
    )
    def test_boolean_rule_correct(self, value, prop):
        self.assertIsInstance(
            ValidatorRules.values(value=value, prop=prop).boolean(), ValidatorRules
        )

    def test_throw_a_validation_exception_when_two_or_more_rules(self):
        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value=None, prop="prop").required().string().boolean()
        self.assertEqual("prop is required", str(assert_error.exception))

        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value=5, prop="prop").required().string()
        self.assertEqual("prop must be a string", str(assert_error.exception))

        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value="test", prop="prop").required().max_length(3)
        self.assertEqual(
            "prop must be less than 3 characters", str(assert_error.exception)
        )

        with self.assertRaises(Exception) as assert_error:
            ValidatorRules.values(value="test", prop="prop").string().boolean()
        self.assertEqual("prop must be a boolean", str(assert_error.exception))

    def test_case_valid_for_many_rules(self):
        ValidatorRules.values(value="test", prop="prop").required().string()
        ValidatorRules.values(value="test", prop="prop").required().max_length(4)
        ValidatorRules.values(value=True, prop="prop").required().boolean()
        ValidatorRules.values(value=False, prop="prop").required().boolean()
