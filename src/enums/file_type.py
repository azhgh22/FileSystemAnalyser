from __future__ import annotations
import os
import stat
from enum import Enum

class FileType(str,Enum):
    """Enumeration of possible file types (directory, file, symlink, none)."""
    DIR = 'directory'
    FILE = 'file'
    SYMLINK = 'symlink'
    NONE = 'none'

    @staticmethod
    def get_file_type(path: str) -> FileType:
        """Determine the file type of the given path."""
        info = os.lstat(path)
        if stat.S_ISLNK(info.st_mode):
            return FileType.SYMLINK
        elif os.path.isdir(path):
            return FileType.DIR
        elif os.path.isfile(path):
            return FileType.FILE
        return FileType.NONE