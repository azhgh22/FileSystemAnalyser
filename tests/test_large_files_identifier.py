from src.enums.file_type import FileType
from src.file import File
from src.large_file_identifier import LargeFileIdentifier


def test_should_return_only_first_file() -> None:
    identifier = LargeFileIdentifier(400)
    file_list = [
        File(type=FileType.SYMLINK, path='', ext='', size=900, permissions=0o777),
        File(type=FileType.FILE, path='', ext='', size=500, permissions=0o111),
        File(type=FileType.DIR, path='', ext='jpg', size=1000, permissions=0o777),
        File(type=FileType.FILE, path='', ext='html', size=50, permissions=0o777)
    ]

    identified = identifier.identify_large_files(file_list)
    assert len(identified) == 1