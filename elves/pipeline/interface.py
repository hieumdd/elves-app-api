from typing import Any, Callable
from dataclasses import dataclass

@dataclass
class Pipeline:
    name: str
    url: str
    transform: Callable[[list[dict]], list[dict]]
    schema: list[dict[str, Any]]
