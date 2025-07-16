from src.file import File


class OddPermission:
    """Base class for identifying files with specific odd permissions."""
    def __init__(self,permission_to_compare:int,name: str) -> None:
        """Initialize with a permission mask and a name for the permission type."""
        self.files: list[File] = []
        self.permission_to_compare: int = permission_to_compare
        self.name = name

    def identify_odd_files(self, file: File) -> bool:
        """Identify if the file has the odd permission and store it if so."""
        if (file.permissions & self.permission_to_compare) != 0:
            self.files.append(file)
            return True

        return False

    def report(self) -> None:
        """Print a report of all files with this odd permission."""
        print(f'\n{self.name} : ')
        for file in self.files:
            print(f'\t{file.path}')