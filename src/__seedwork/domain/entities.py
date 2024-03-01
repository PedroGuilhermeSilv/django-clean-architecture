from dataclasses import dataclass, field, asdict
from src.__seedwork.domain.value_objects import UniqueEntityId
from abc import ABC
from typing import Any


@dataclass(frozen=True)
class Entity(ABC):
    unique_entity_id: UniqueEntityId = field(default_factory=lambda: UniqueEntityId())

    @property
    def id(self):
        return str(self.unique_entity_id)

    def to_dict(self):
        entity_dict = asdict(self)
        entity_dict.pop("unique_entity_id")
        entity_dict["id"] = self.id
        return entity_dict

    def _set(self, name: str, value: Any):
        object.__setattr__(self, name, value)
        return self
