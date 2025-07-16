from src.file import File


class OddPermission:
    def __init__(self,permission_to_compare:int,name: str) -> None:
        self.files: list[File] = []
        self.permission_to_compare: int = permission_to_compare
        self.name = name

    def identify_odd_files(self, file: File) -> bool:
        if (file.permissions & self.permission_to_compare) != 0:
            self.files.append(file)
            return True

        return False

    def report(self) -> None:
        print(f'\n{self.name} : ')
        for file in self.files:
            print(f'\t{file.path}')