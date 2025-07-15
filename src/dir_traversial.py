import os
from dataclasses import dataclass
from typing import Protocol

from src.enums.file_type import FileType


@dataclass
class File:
    type: str
    path: str
    ext: str
    size: int
    permissions: int


class DirTraversal(Protocol):
    def traverse(self) -> list[File]:
        pass

@dataclass
class StandardDirTraversal:
    dir_path: str
    follow_symlinks: bool = False

    def __post_init__(self) -> None:
        if not os.path.exists(self.dir_path):
            raise FileNotFoundError(f"❌ Path '{self.dir_path}' does not exist.")
        if not os.path.isdir(self.dir_path):
            raise ValueError(f"❌ Path '{self.dir_path}' is not a directory.")

    def traverse(self) -> list[File]:
        file_list = []
        self.__traverse_helper(self.dir_path, file_list)
        return file_list

    def __traverse_helper(self,cur_path:str,file_list) -> None:
        with os.scandir(cur_path) as entries:
            for entry in entries:
                path = entry.path
                size = entry.stat().st_size
                permissions = entry.stat().st_mode & 0o777
                ext = self.extract_extentions(entry.name)
                file_type = self.get_file_type(entry.path)
                file_list.append(File(type=file_type, path=path, ext=ext, size=size, permissions=permissions))

                if entry.is_dir(follow_symlinks=False):
                    self.__traverse_helper(entry.path, file_list)

    def extract_extentions(self,name: str) -> str:
        if '.' in name:
            return name.split('.')[-1]
        return ''

    def get_file_type(self, path: str) -> FileType:
        if os.path.isdir(path):
            return FileType.DIR
        elif os.path.isfile(path):
            return FileType.FILE
        return FileType.NONE
