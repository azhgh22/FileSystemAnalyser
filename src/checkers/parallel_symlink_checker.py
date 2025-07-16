import os
from dataclasses import dataclass
from queue import Queue
from typing import Any, Callable

from src.enums.file_type import FileType
from src.file import File


@dataclass
class ParallelSymlinkChecker:
    """Checker to validate and optionally follow symlinked directories."""
    follow_links:bool

    def validate(self,file:File,callback:Callable[..., Any], *args: Any) -> bool:
        """Validate if a symlink should be followed and invoke callback if so."""
        dir_queue, visited_inodes, visited_inodes_lock, file_list, file_list_lock = args
        if file.type == FileType.SYMLINK and os.path.isdir(file.path) and self.follow_links:
            dir_queue.put(file.path)
            callback(*args)
            return True

        return False
