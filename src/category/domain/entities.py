from datetime import datetime
from dataclasses import  dataclass, field
from typing import Optional
import uuid

@dataclass
class Category(kw_only=True):
    id: uuid.UUID = field(default_factory=lambda: uuid.uuid4())
    name: Optional[str]
    description: Optional[str] = None
    is_activate: Optional[bool] = True
    created_at: Optional[datetime] = field(default_factory=lambda: datetime.now())
    


