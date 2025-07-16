from src.file_permission_report.odd_permission import OddPermission


# identifies files which are group_writable
#   --- -w- ---
class GroupWritablePermission(OddPermission):
    """Identifies files which are group-writable."""
    def __init__(self) -> None:
        """Initialize with the permission mask for group-writable files."""
        super().__init__(0o020,'GroupWritable')