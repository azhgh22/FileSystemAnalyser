from dataclasses import dataclass
from queue import Queue
from typing import Callable, Any

from src.enums.file_type import FileType
from src.file import File


@dataclass
class ParallelPermissionChecker:
    """Checker to validate directory read permissions."""
    permission_to_validate:int
    ignore_not_readable_dirs:bool

    def validate(self,file:File,callback:Callable[..., Any], *args: Any) -> bool:
        """Validate if a directory is readable and invoke callback if so."""
        dir_queue, visited_inodes, visited_inodes_lock, file_list, file_list_lock = args
        if file.type == FileType.DIR:
            if file.permissions & self.permission_to_validate == 0:
                if self.ignore_not_readable_dirs:
                    return False
                else:
                    raise ValueError(f"'{file.path}' is not readable")
            else:
                dir_queue.put(file.path)
                callback(*args)
                return True


        return False