from src.file_permission_report.odd_permission import OddPermission


# identifies files which are writeable for all users
#   - --- --- rw-
class WorldWritablePermission(OddPermission):
    """Identifies files which are writable for all users (world-writable)."""
    def __init__(self) -> None:
        """Initialize with the permission mask for world-writable files."""
        super().__init__(0o002,'WorldWritable')