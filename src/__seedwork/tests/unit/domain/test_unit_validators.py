import unittest

from __seedwork.domain.validators import ValidatorRules


class TestValidorRules(unittest.TestCase):
    def test_values_method(self):
        validator = ValidatorRules.values("value", "prop")
        self.assertIsInstance(validator, ValidatorRules)
        self.assertEqual(validator.value, "value")
        self.assertEqual(validator.prop, "prop")

    def test_required_rule(self):
        invalid_values = [
            {"value": None, "prop": "prop"},
            {"value": "", "prop": "prop"},
        ]
        for data in invalid_values:
            with self.assertRaises(Exception) as assert_error:
                self.assertIsInstance(
                    ValidatorRules.values(data["value"], data["prop"]).required(),
                    ValidatorRules,
                )

            self.assertEqual("prop is required", str(assert_error.exception))
