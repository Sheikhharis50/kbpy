from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass(kw_only=True)
class Model:
    id: UUID = field(default_factory=uuid4, init=False)
    created_at: datetime = field(default_factory=datetime.now, init=False)
    updated_at: datetime = field(default_factory=datetime.now, init=False)

    def save(self, update: bool = False, **kwargs):
        for field in self.__annotations__.keys():
            if field not in kwargs:
                continue

            setattr(self, field, kwargs.get(field))

        if update:
            self.updated_at = datetime.now()
