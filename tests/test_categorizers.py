import pytest

from src.categorizers.categories.image_categorizer import ImageCategorizer
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
