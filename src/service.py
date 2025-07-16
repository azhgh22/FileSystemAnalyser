from typing import Protocol

from src.file import File


# Protocol for services that process files and generate reports.
class Service(Protocol):
    """Protocol for services that process files and generate reports."""
    def fit(self, file: File) -> File:
        """Process a file and return the (possibly modified) file."""
        pass

    def make_report(self) -> None:
        """Generate and output a report based on processed files."""
        pass