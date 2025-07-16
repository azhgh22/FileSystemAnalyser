from typing import Protocol

from src.file import File



class DirTraversal(Protocol):
    """Protocol for directory traversal strategies."""
    def traverse(self) -> list[File]:
        """Traverse a directory and return a list of File objects."""
        pass