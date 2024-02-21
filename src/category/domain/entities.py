from datetime import datetime
from dataclasses import dataclass, field
from typing import Optional

from src.__seedwork.domain.entities import Entity


@dataclass(frozen=True, kw_only=True, slots=True)
class Category(Entity):
    name: Optional[str]
    description: Optional[str] = None
    is_activate: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())
