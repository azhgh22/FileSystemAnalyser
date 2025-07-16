from src.file_permission_report.odd_permission import OddPermission


# identifies files which are writeable for all users
#   - --- --- rw-
class WorldWritablePermission(OddPermission):
    def __init__(self) -> None:
        super().__init__(0o002,'WorldWritable')