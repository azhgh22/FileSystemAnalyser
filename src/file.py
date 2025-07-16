from dataclasses import dataclass

from src.enums.file_category import FileCategory


@dataclass
class File:
    type: str
    path: str
    ext: str
    size: int
    permissions: int
    category:FileCategory = 'undefined'

    def __str__(self) -> str:
        return f'{self.path} {self.type} {self.permissions} {self.ext} {self.size} {self.category}'