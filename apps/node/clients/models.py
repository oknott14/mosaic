from abc import ABC
from dataclasses import dataclass, field
from typing import Any, Dict


@dataclass
class HttpResponse(ABC):
    status: int


@dataclass
class HttpPostResponse(HttpResponse):
    body: Dict[Any, Any] = field(default_factory=dict)
