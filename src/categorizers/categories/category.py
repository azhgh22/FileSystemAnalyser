import magic

from src.enums.file_category import FileCategory
from src.file import File


class Category:
    def __init__(self,total_size:int,mime_type:list[str],image_extension:list[str],category_type:FileCategory) -> None:
        self.total_size = total_size
        self.mime_type = mime_type
        self.image_extension = image_extension
        self.category_type = category_type

    def categorize(self, file: File) -> File:
        ext_categorized = self.__categorize_with_extension(file)
        if ext_categorized.category == FileCategory.UNDEFINED:
            file = self.__categorize_with_magic_number(file)

        return file

    def get_total_size(self) -> int:
        return self.total_size

    def __categorize_with_extension(self, file: File) -> File:
        if file.ext in self.image_extension:
            file.category = self.category_type
            self.total_size = self.total_size + file.size
        return file

    def __categorize_with_magic_number(self, file: File) -> File:
        try:
            mime = magic.Magic(mime=True)
            mime_type = mime.from_file(file.path)
            if mime_type in self.mime_type:
                file.category = self.category_type
                self.total_size = self.total_size + file.size
        except PermissionError:
            pass
        except IsADirectoryError:
            pass

        return file