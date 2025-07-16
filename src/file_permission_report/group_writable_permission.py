from src.file_permission_report.odd_permission import OddPermission


# identifies files which are group_writable
#   --- -w- ---
class GroupWritablePermission(OddPermission):
    def __init__(self) -> None:
        super().__init__(0o020,'GroupWritable')