from typing import Protocol

from src.file import File


class DirTraversal(Protocol):
    def traverse(self) -> list[File]:
        pass