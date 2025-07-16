from typing import Protocol

from src.file import File


class TypeCategorizer(Protocol):
    def categorize(self,files:list[File]) -> list[File]:
        pass