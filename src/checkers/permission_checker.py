from dataclasses import dataclass
from typing import Callable, Any

from src.enums.file_type import FileType
from src.file import File


@dataclass
class PermissionChecker:
    permission_to_validate:int
    ignore_not_readable_dirs:bool

    def validate(self,file:File,callback:Callable[..., Any], *args: Any) -> bool:
        if file.type == FileType.DIR:
            if file.permissions & self.permission_to_validate == 0:
                if self.ignore_not_readable_dirs:
                    return False
                else:
                    raise ValueError(f"'{file.path}' is not readable")
            else:
                callback(*args)
                return True


        return False