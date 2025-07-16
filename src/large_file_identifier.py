from src.enums.file_type import FileType
from src.file import File


class LargeFileIdentifier:
    def __init__(self, size_threshold:int) -> None:
        self.size_threshold = size_threshold
        self.large_files:list[File] = []

    def identify_large_files(self,files:list[File]) -> list[File]:
        self.large_files = list(filter(lambda x: (x.size > self.size_threshold and x.type==FileType.FILE), files))
        return self.large_files

    def make_report(self) -> None:
        print('\n\nLarge Files')
        for file in self.large_files:
            print(file)

        print('\n')
