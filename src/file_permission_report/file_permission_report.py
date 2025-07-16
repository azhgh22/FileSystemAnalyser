from src.file import File
from src.file_permission_report.group_writable_permission import GroupWritablePermission
from src.file_permission_report.odd_permission import OddPermission
from src.file_permission_report.world_executable_permission import WorldExecutablePermission
from src.file_permission_report.world_writable_permission import WorldWritablePermission


class FilePermissionReport:
    """Aggregates and reports on files with odd permissions (group/world writable/executable)."""
    def __init__(self) -> None:
        """Initialize with a list of odd permission checkers."""
        self.odd_permission:list[OddPermission] = [
            GroupWritablePermission(),
            WorldExecutablePermission(),
            WorldWritablePermission(),
        ]

    def fit(self,file:File) -> File:
        """Check the file against all odd permission checkers."""
        for perms in self.odd_permission:
            perms.identify_odd_files(file)

        return file

    def make_report(self) -> None:
        """Print a report of all files with odd permissions."""
        print('\n\nFile Permissions Report')
        for perms in self.odd_permission:
            perms.report()
        print('\n')