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
        thread_id, thread_states, thread_condition, queue_lock, dir_queue, visited_inodes, visited_inodes_lock, file_list, file_list_lock = args
        if file.type == FileType.SYMLINK and os.path.isdir(file.path) and self.follow_links:
            queue_lock.acquire()
            dir_queue.put(file.path)
            thread_condition.notify(1)
            queue_lock.release()
            # callback(*args)
            return True

        return False
