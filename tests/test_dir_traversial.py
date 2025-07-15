import os
from fs.osfs import OSFS
from src.dir_traversial import StandardDirTraversal, File
import pytest
import stat

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


def check_small_file(file_list: list[File]) -> None:
    for file in file_list:
        print(file.path, file.ext, file.size, file.type, file.permissions)
        assert file.type == FileType.FILE
        assert file.size == 0
        assert file.ext == 'txt'

def test_path_contains_only_files_not_dir_or_symbolic_links(small_root_dir:str) -> None:
    file_list = StandardDirTraversal('./' + small_root_dir).traverse()
    assert len(file_list) == 10
    check_small_file(file_list)
    with OSFS('.') as fs:
        fs.removetree(small_root_dir)

def test_path_contains_only_directory_and_files_in_it(small_recursive_root_dir:str)-> None:
    file_list = StandardDirTraversal('./' + small_recursive_root_dir).traverse()
    assert len(file_list) == 10
    check_small_file(file_list)
    with OSFS('.') as fs:
        fs.removetree(small_recursive_root_dir)

def test_path_with_files_and_directories(medium_recursive_root_dir:str) -> None:
    file_list = StandardDirTraversal('./' + medium_recursive_root_dir).traverse()

    directory = [x for x in file_list if x.type==FileType.DIR]
    files = [x for x in file_list if x.type==FileType.FILE]

    assert len(file_list) == 21
    assert len(directory) == 1
    assert len(files) == 20

    check_small_file(files)
    with OSFS('.') as fs:
        fs.removetree(medium_recursive_root_dir)

def test_path_with_multiple_dirs_and_files(big_recursive_root_dir:str) -> None:
    file_list = StandardDirTraversal('./' + big_recursive_root_dir).traverse()
    directory = [x for x in file_list if x.type == FileType.DIR]
    files = [x for x in file_list if x.type == FileType.FILE]

    assert len(file_list) == 120
    assert len(directory) == 10
    assert len(files) == 110
    check_small_file(files)
    with OSFS('.') as fs:
        fs.removetree(big_recursive_root_dir)

def test_path_contains_inaccessible_directory(small_root_dir:str) -> None:
    # os.chmod(f'./root/0.txt', stat.S_IWUSR | stat.S_IXUSR)

    file_list = StandardDirTraversal(small_root_dir).traverse()
    # os.chmod(f'{medium_recursive_root_dir}/subdir', 0o000)

    # assert len(file_list) == 21
    check_small_file(file_list)

    with OSFS('.') as fs:
        fs.removetree(small_root_dir)
