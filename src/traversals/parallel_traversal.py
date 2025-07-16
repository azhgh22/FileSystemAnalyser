import os
import threading
from dataclasses import dataclass, field
from typing import Any

from src.checkers.checker import Checker
from src.checkers.parallel_permission_checker import ParallelPermissionChecker
from src.checkers.parallel_symlink_checker import ParallelSymlinkChecker
from src.enums.file_type import FileType
from src.file import File
from src.service import Service
from queue import Queue


@dataclass
class ParallelTraversal:
    """Performs a parallel directory traversal, work distributed among n workers ,
     applying checkers and services to files."""
    dir_path: str
    follow_symlinks: bool = False
    ignore_inaccessible_files: bool = True
    checkers:list[Checker] = field(default_factory=lambda: [])
    services:list[Service] = field(default_factory=lambda: [])
    num_workers:int = os.cpu_count()

    def __post_init__(self) -> None:
        """Validate the directory path and initialize checkers if not provided."""
        if not os.path.exists(self.dir_path):
            raise FileNotFoundError(f"Path '{self.dir_path}' does not exist.")
        if not os.path.isdir(self.dir_path):
            raise ValueError(f"Path '{self.dir_path}' is not a directory.")
        if len(self.checkers) != 0: return
        self.checkers = [ParallelPermissionChecker(0o400, self.ignore_inaccessible_files),
                         ParallelSymlinkChecker(self.follow_symlinks)]
        self.workers:list[threading.Thread] = []

    def traverse(self) -> list[File]:
        """Traverse the directory and return a list of File objects."""
        file_list = []
        info = os.stat(self.dir_path)
        visited_inodes:set[tuple[int,int]] = set()
        visited_inodes.add((info.st_dev,info.st_ino))

        dir_queue = Queue()
        dir_queue.put(self.dir_path)
        visited_inodes_lock = threading.Lock()
        file_list_lock = threading.Lock()

        for i in range(self.num_workers):
            thread = threading.Thread(target=self.__traverse_helper,
                                                 args=(dir_queue,
                                                       visited_inodes,
                                                       visited_inodes_lock,
                                                       file_list,
                                                       file_list_lock) )
            self.workers.append(thread)
            thread.start()

        for thread in self.workers:
            thread.join()

        return file_list

    def __traverse_helper(self,
                          dir_queue:Queue[str],
                          visited_inodes:set[tuple[int,int]],
                          visited_inodes_lock:threading.Lock,
                          file_list:list[File],
                          file_list_lock:threading.Lock) -> None:
        """Helper function to recursively traverse directories."""
        cur_path = dir_queue.get()

        with os.scandir(cur_path) as entries:
            for entry in entries:
                path = entry.path
                size = entry.stat().st_size
                permissions = entry.stat().st_mode & 0o777
                ext = entry.name.split('.')[-1] if '.' in entry.name else ''
                file_type = FileType.get_file_type(entry.path)
                new_file = File(type=file_type, path=path, ext=ext, size=size, permissions=permissions)

                for service in self.services:
                    service.fit(new_file)

                with file_list_lock:
                    file_list.append(new_file)

                with visited_inodes_lock:
                    if (entry.stat().st_dev,entry.stat().st_ino) in visited_inodes:
                        continue
                    visited_inodes.add((entry.stat().st_dev, entry.stat().st_ino))


                self.__validate_checkers(new_file,dir_queue,visited_inodes,visited_inodes_lock,file_list,file_list_lock)


    def __validate_checkers(self,file:File,*args:Any) -> None:
        """Run all checkers on the given file and arguments."""
        for checker in self.checkers:
            if checker.validate(file,self.__traverse_helper,*args):
                return