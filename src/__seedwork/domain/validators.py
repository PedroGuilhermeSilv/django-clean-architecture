from dataclasses import dataclass
from typing import Any
from src.__seedwork.domain.exceptions import ValidationException


@dataclass(frozen=True, slots=True)
class ValidatorRules:
    value: Any
    prop: str

    @staticmethod
    def values(value: Any, prop: str):
        return ValidatorRules(value, prop)

    def required(self) -> "ValidatorRules":
        if self.value is None or self.value == "":
            raise ValidationException(f"{self.prop} is required")
        return self

    def string(self) -> "ValidatorRules":
        if not isinstance(self.value, str):
            raise ValidationException(f"{self.prop} must be a string")
        return self

    def max_length(self, max: int) -> "ValidatorRules":
        if len(self.value) > max:
            raise ValidationException(f"{self.prop} must be less than {max} characters")
        return self

    def boolean(self) -> "ValidatorRules":
        if self.value is not True and self.value is not False:
            raise ValidationException(f"{self.prop} must be a boolean")
        return self