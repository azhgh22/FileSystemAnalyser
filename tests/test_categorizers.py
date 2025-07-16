import os

import pytest

from src.categorizers.categories.executable_categorizer import ExecutableCategorizer
from src.categorizers.categories.image_categorizer import ImageCategorizer
from src.categorizers.categories.text_categorizer import TextCategorizer
from src.categorizers.categories.video_categorizer import VideoCategorizer
from src.categorizers.simple_categorizer import SimpleCategorizer
from src.enums.file_category import FileCategory
from src.enums.file_type import FileType
from src.file import File

@pytest.fixture
def file() -> File:
    return File(type=FileType.FILE,path='',ext='',size=50,permissions=0o777)

def test_should_categorize_file_as_image(file:File) -> None:
    categorizer = ImageCategorizer()
    file.path = './test_files/horse.jpg'
    file.ext = 'jpg'

    assert categorizer.categorize(file).category == FileCategory.IMAGE
    assert categorizer.get_total_size() == 50

def test_should_categorize_file_with_no_extension_as_image(file:File) -> None:
    categorizer = ImageCategorizer()
    file.path = './test_files/horse.jpg'
    file.ext = ''
    assert categorizer.categorize(file).category == FileCategory.IMAGE
    assert categorizer.get_total_size() == 50

def test_should_not_categorize_not_readable_file_with_no_extension_as_executable_with_permissions(file:File) -> None:
    os.chmod('./test_files/babyrop_level_not_readable', 0o111)
    categorizer = ExecutableCategorizer()
    file.path = './test_files/babyrop_level_not_readable'
    file.permissions = 0o211
    assert categorizer.categorize(file).category == FileCategory.UNDEFINED
    assert categorizer.get_total_size() == 0
    os.chmod('./test_files/babyrop_level_not_readable', 0o777)

def test_should_categorize_file_as_executable(file:File) -> None:
    categorizer = ExecutableCategorizer()
    file.path = './test_files/babyrop_level15.0'

    assert categorizer.categorize(file).category == FileCategory.EXECUTABLE
    assert categorizer.get_total_size() == 50

def test_should_categorize_file_as_text(file:File) -> None:
    categorizer = TextCategorizer()
    file.path = './test_files/main.html'
    file.ext = 'html'

    assert categorizer.categorize(file).category == FileCategory.TEXT
    assert categorizer.get_total_size() == 50

def test_should_categorize_file_as_video(file:File) -> None:
    categorizer = VideoCategorizer()
    file.ext = 'mp4'

    assert categorizer.categorize(file).category == FileCategory.VIDEO
    assert categorizer.get_total_size() == 50

def test_should_categorize_all_files() -> None:
    os.chmod('./test_files/babyrop_level_not_readable', 0o111)
    file_list = [
        File(type=FileType.FILE, path='./test_files/babyrop_level15.0', ext='', size=50, permissions=0o777),
        File(type=FileType.FILE, path='./test_files/babyrop_level_not_readable', ext='', size=50, permissions=0o111),
        File(type=FileType.FILE, path='./test_files/horse.jpg', ext='jpg', size=50, permissions=0o777),
        File(type=FileType.FILE, path='./test_files/main.html', ext='html', size=50, permissions=0o777)
    ]

    categorizer = SimpleCategorizer([ExecutableCategorizer(),VideoCategorizer(),TextCategorizer(),ImageCategorizer()])
    result = categorizer.categorize(file_list)
    img = [x for x in result if x.category==FileCategory.IMAGE]
    video = [x for x in result if x.category == FileCategory.VIDEO]
    executable = [x for x in result if x.category == FileCategory.EXECUTABLE]
    text = [x for x in result if x.category == FileCategory.TEXT]

    assert len(img) == 1
    assert len(video) == 0
    assert len(executable) == 1
    assert len(text) == 1

    os.chmod('./test_files/babyrop_level_not_readable', 0o777)

