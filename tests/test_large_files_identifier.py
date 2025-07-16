from src.enums.file_type import FileType
from src.file import File
from src.large_file_identifier import LargeFileIdentifier


def test_should_return_only_first_file() -> None:
    identifier = LargeFileIdentifier(400)
    file_list = File(type=FileType.FILE, path='', ext='', size=900, permissions=0o777)

    assert len(identifier.large_files) == 0
    identifier.fit(file_list)
    assert len(identifier.get_files()) == 1