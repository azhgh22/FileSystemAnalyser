from dataclasses import dataclass
from typing import Any, Callable

from src.enums.file_type import FileType
from src.file import File


@dataclass
class SymlinkChecker:
    follow_links:bool

    def validate(self,file:File,callback:Callable[..., Any], *args: Any) -> bool:
        if file.type == FileType.SYMLINK and self.follow_links:
            callback(*args)
            return True

        return False
