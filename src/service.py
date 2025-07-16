from typing import Protocol

from src.file import File


class Service(Protocol):
    def fit(self, file: File) -> File:
        pass

    def make_report(self) -> None:
        pass