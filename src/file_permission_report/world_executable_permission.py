from src.file_permission_report.odd_permission import OddPermission


# identifies files which are executable for all users
#   - --- --- --x
class WorldExecutablePermission(OddPermission):
    """Identifies files which are executable for all users (world-executable)."""
    def __init__(self) -> None:
        """Initialize with the permission mask for world-executable files."""
        super().__init__(0o001,"WorldExecutable")