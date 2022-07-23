from typing import Any
from dataclasses import dataclass

@dataclass
class Pipeline:
    name: str
    url: str
    schema: list[dict[str, Any]]
