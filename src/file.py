from dataclasses import dataclass
from typing import Any


@dataclass
class File:
    type: str
    path: str
    ext: str
    size: int
    permissions: int

    # def __eq__(self, other: Any) -> bool:
    #     pass