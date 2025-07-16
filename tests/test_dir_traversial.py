import os
from fs.osfs import OSFS
from src.traversals.standard_dir_traversal import StandardDirTraversal, File
import pytest

from src.enums.file_type import FileType


@pytest.fixture
def small_root_dir() -> str:
    # remove if exists
    if os.path.exists('./root'):
        with OSFS('.') as fs:
            fs.removetree('root')

    os.mkdir('root')
    for i in range(10):
        open(f"root/{i}.txt", "a").close()

    return 'root'

@pytest.fixture
def small_recursive_root_dir() -> str:
    # remove if exists
    if os.path.exists('./root'):
        with OSFS('.') as fs:
            fs.removetree('root')

    os.mkdir('root')
    os.mkdir('root/subdir')
    for i in range(10):
        open(f"root/subdir/{i}.txt", "a").close()

    return 'root'

@pytest.fixture
def medium_recursive_root_dir() -> str:
    # remove if exists
    if os.path.exists('./root'):
        with OSFS('.') as fs:
            fs.removetree('root')

    os.mkdir('root')
    for i in range(10):
        open(f"root/{i}.txt", "a").close()

    os.mkdir('root/subdir')
    for i in range(10):
        open(f"root/subdir/{i}.txt", "a").close()

    return 'root'


@pytest.fixture
def big_recursive_root_dir() -> str:
    # remove if exists
    if os.path.exists('./root'):
        with OSFS('.') as fs:
            fs.removetree('root')

    os.mkdir('root')
    for i in range(10):
        open(f"root/{i}.txt", "a").close()

    for i in range(10):
        os.mkdir(f'root/subdir{i}')
        for j in range(10):
            open(f"root/subdir{i}/{j}.txt", "a").close()

    return 'root'

@pytest.fixture
def root_with_symlink() -> str:
    # remove if exists
    if os.path.exists('./root'):
        try:
            os.unlink("./root/src")
        except OSError:
            pass
        with OSFS('.') as fs:
            fs.removetree('root')

    os.mkdir('root')
    for i in range(10):
        open(f"root/{i}.txt", "a").close()

    # open(f"root/src", "a").close()
    os.symlink('../root','./root/src')

    return 'root'


def check_small_file(file_list: list[File]) -> None:
    for file in file_list:
        print(file.path, file.ext, file.size, file.type, file.permissions)
        assert file.type == FileType.FILE
        assert file.size == 0
        assert file.ext == 'txt'

def traverse_checker(file_list:list[File],full_count:int,dir_count,file_count:int) -> None:
    directory = [x for x in file_list if x.type == FileType.DIR]
    files = [x for x in file_list if x.type == FileType.FILE]

    assert len(file_list) == full_count
    assert len(directory) == dir_count
    assert len(files) == file_count
    check_small_file(files)

def test_path_does_not_exist() -> None:
    try:
        StandardDirTraversal('./bla').traverse()
        assert False
    except FileNotFoundError:
        assert True

def test_path_is_not_dir() -> None:
    open("empty.txt", "a").close()
    try:
        StandardDirTraversal('./empty.txt').traverse()
        assert False
    except ValueError:
        assert True
    os.remove("empty.txt")

def test_path_is_empty() -> None:
    os.mkdir("root")
    assert StandardDirTraversal('./root').traverse() == []
    os.rmdir("root")

def test_path_contains_only_files_not_dir_or_symbolic_links(small_root_dir:str) -> None:
    file_list = StandardDirTraversal('./' + small_root_dir).traverse()
    traverse_checker(file_list,10,0,10)
    with OSFS('.') as fs:
        fs.removetree(small_root_dir)

def test_path_contains_only_directory_and_files_in_it(small_recursive_root_dir:str)-> None:
    file_list = StandardDirTraversal('./' + small_recursive_root_dir).traverse()
    print('file_count: ', len(file_list))
    traverse_checker(file_list,11,1,10)
    with OSFS('.') as fs:
        fs.removetree(small_recursive_root_dir)

def test_path_with_files_and_directories(medium_recursive_root_dir:str) -> None:
    file_list = StandardDirTraversal('./' + medium_recursive_root_dir).traverse()
    traverse_checker(file_list, 21, 1, 20)
    with OSFS('.') as fs:
        fs.removetree(medium_recursive_root_dir)

def test_path_with_multiple_dirs_and_files(big_recursive_root_dir:str) -> None:
    file_list = StandardDirTraversal('./' + big_recursive_root_dir).traverse()
    traverse_checker(file_list, 120, 10, 110)
    with OSFS('.') as fs:
        fs.removetree(big_recursive_root_dir)

def test_path_contains_inaccessible_directory(medium_recursive_root_dir:str) -> None:
    os.chmod(f'{medium_recursive_root_dir}/subdir', 0o111)
    file_list = StandardDirTraversal(medium_recursive_root_dir).traverse()
    traverse_checker(file_list,11,1,10)
    os.chmod(f'{medium_recursive_root_dir}/subdir', 0o777)
    with OSFS('.') as fs:
        fs.removetree(medium_recursive_root_dir)

def test_path_contains_symlink_to_directory_and_do_not_follow_symlinks(root_with_symlink:str)-> None:
    file_list = StandardDirTraversal(root_with_symlink,follow_symlinks=False).traverse()
    symlink = [x for x in file_list if x.type == FileType.SYMLINK]
    files = [x for x in file_list if x.type == FileType.FILE]

    assert len(file_list) == 11
    assert len(symlink) == 1
    assert len(files) == 10
    check_small_file(files)

    print('file_count: ',len(file_list))
    for file in file_list:
        print(file.path, file.ext, file.size, file.type, file.permissions)

    os.unlink("./root/src")
    with OSFS('.') as fs:
        fs.removetree(root_with_symlink)


def test_path_contains_symlink_to_directory_and_follow_symlinks_with_cycle(root_with_symlink:str)-> None:
    file_list = StandardDirTraversal(root_with_symlink,follow_symlinks=True).traverse()
    assert len(file_list) == 11
    os.unlink("./root/src")
    with OSFS('.') as fs:
        fs.removetree(root_with_symlink)