from dataclasses import dataclass

from src.enums.file_category import FileCategory


@dataclass
class File:
    """Represents a file with its metadata and category."""
    type: str
    path: str
    ext: str
    size: int
    permissions: int
    category:FileCategory = 'undefined'

    def __str__(self) -> str:
        """Return a string representation of the file's metadata."""
        return f'{self.path} {self.type} {self.permissions} {self.ext} {self.size} {self.category}'