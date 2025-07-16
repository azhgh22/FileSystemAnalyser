from src.enums.file_type import FileType
from src.file import File


class LargeFileIdentifier:
    def __init__(self, size_threshold:int) -> None:
        self.size_threshold = size_threshold
        self.large_files:list[File] = []

    def fit(self,file:File) -> File:
        if file.size > self.size_threshold and file.type==FileType.FILE:
            self.large_files.append(file)

        return file

    def make_report(self) -> None:
        print('\n\nLarge Files')
        for file in self.large_files:
            print(file)

        print('\n')

    def get_files(self) -> list[File]:
        return self.large_files
