from src.file_permission_report.odd_permission import OddPermission


# identifies files which are executable for all users
#   - --- --- --x
class WorldExecutablePermission(OddPermission):
    def __init__(self) -> None:
        super().__init__(0o001,"WorldExecutable")