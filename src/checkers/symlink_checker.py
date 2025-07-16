import os
from dataclasses import dataclass
from typing import Any, Callable

from src.enums.file_type import FileType
from src.file import File


@dataclass
class SymlinkChecker:
    """Checker to validate and optionally follow symlinked directories."""
    follow_links:bool

    def validate(self,file:File,callback:Callable[..., Any], *args: Any) -> bool:
        """Validate if a symlink should be followed and invoke callback if so."""
        if file.type == FileType.SYMLINK and os.path.isdir(file.path) and self.follow_links:
            callback(*args)
            return True

        return False
