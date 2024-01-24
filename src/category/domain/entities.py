from datetime import datetime
from dataclasses import  dataclass, field
from typing import Optional

class Category():
    name: Optional[str]
    description: Optional[str] = None
    is_activate: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())


