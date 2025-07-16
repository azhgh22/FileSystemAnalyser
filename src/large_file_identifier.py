from src.enums.file_type import FileType
from src.file import File


# Identifies and stores files larger than a specified size threshold.
class LargeFileIdentifier:
    """Class to identify and store files exceeding a given size threshold."""
    def __init__(self, size_threshold:int) -> None:
        """Initialize with a size threshold and prepare storage for large files."""
        self.size_threshold = size_threshold
        self.large_files:list[File] = []

    def fit(self,file:File) -> File:
        """Check if the file exceeds the size threshold and store it if so."""
        if file.size > self.size_threshold and file.type==FileType.FILE:
            self.large_files.append(file)

        return file

    def make_report(self) -> None:
        """Print a report of all large files identified."""
        print('\n\nLarge Files')
        for file in self.large_files:
            print(file)

        print('\n')

    def get_files(self) -> list[File]:
        """Return the list of large files."""
        return self.large_files
