import os
from dataclasses import dataclass, field
from typing import Any

from src.checkers.checker import Checker
from src.checkers.permission_checker import PermissionChecker
from src.checkers.symlink_checker import SymlinkChecker
from src.enums.file_type import FileType
from src.file import File


@dataclass
class StandardDirTraversal:
    dir_path: str
    follow_symlinks: bool = False
    ignore_inaccessible_files: bool = True
    checkers:list[Checker] = field(default_factory=lambda: [])

    def __post_init__(self) -> None:
        if not os.path.exists(self.dir_path):
            raise FileNotFoundError(f"Path '{self.dir_path}' does not exist.")
        if not os.path.isdir(self.dir_path):
            raise ValueError(f"Path '{self.dir_path}' is not a directory.")
        if len(self.checkers) != 0: return
        self.checkers = [PermissionChecker(0o400, self.ignore_inaccessible_files), SymlinkChecker(self.follow_symlinks)]

    def traverse(self) -> list[File]:
        file_list = []
        info = os.stat(self.dir_path)
        visited_inodes:set[tuple[int,int]] = set()
        visited_inodes.add((info.st_dev,info.st_ino))
        self.__traverse_helper(self.dir_path, file_list,visited_inodes)
        return file_list

    def __traverse_helper(self,cur_path:str,file_list,visited_inodes:set[tuple[int,int]]) -> None:
        with os.scandir(cur_path) as entries:
            for entry in entries:
                path = entry.path
                size = entry.stat().st_size
                permissions = entry.stat().st_mode & 0o777
                ext = entry.name.split('.')[-1] if '.' in entry.name else ''
                file_type = FileType.get_file_type(entry.path)
                new_file = File(type=file_type, path=path, ext=ext, size=size, permissions=permissions)
                file_list.append(new_file)

                if (entry.stat().st_dev,entry.stat().st_ino) in visited_inodes:
                    continue

                visited_inodes.add((entry.stat().st_dev, entry.stat().st_ino))

                self.__validate_checkers(new_file,entry.path,file_list,visited_inodes)


    def __validate_checkers(self,file:File,*args:Any) -> None:
        for checker in self.checkers:
            if checker.validate(file,self.__traverse_helper,*args):
                return