from asyncio import Protocol
from dataclasses import dataclass, field

import magic

from src.enums.file_category import FileCategory
from src.file import File


class Category:
    def __init__(self,total_size:int,mime_type:list[str],image_extension:list[str]) -> None:
        self.total_size = total_size
        self.mime_type = mime_type
        self.image_extension = image_extension

    def categorize(self, file: File) -> File:
        ext_categorized = self.__categorize_with_extension(file)
        if ext_categorized.category == FileCategory.UNDEFINED:
            file = self.__categorize_with_magic_number(file)

        return file

    def get_total_size(self) -> int:
        return self.total_size

    def __categorize_with_extension(self, file: File) -> File:
        if file.ext in self.image_extension:
            file.category = FileCategory.IMAGE
            self.total_size = self.total_size + file.size
        return file

    def __categorize_with_magic_number(self, file: File) -> File:
        mime = magic.Magic(mime=True)
        mime_type = mime.from_file(file.path)
        if mime_type in self.mime_type:
            file.category = FileCategory.IMAGE
            self.total_size = self.total_size + file.size

        return file

class ImageCategorizer(Category):
    def __init__(self):
            total_size:int = 0
            mime_type:list[str] = ['image/jpeg']
            image_extension:list[str] = [
                'jpg', 'jpeg',
                'png',                # Portable Network Graphics
                'gif',                # Graphics Interchange Format
                'bmp',                # Bitmap
                'tiff', '.tif',       # Tagged Image File Format
                'webp',               # WebP (Google's image format)
                'svg',                # Scalable Vector Graphics (XML-based)
                'ico',                # Windows icon
                'heic', 'heif',      # High Efficiency Image Format (Apple devices)
                'raw',                # Generic raw image
                'cr2', 'nef', 'orf', 'sr2',  # Camera raw formats (Canon, Nikon, Olympus, Sony)
                'psd',                # Photoshop Document
                'ai',                 # Adobe Illustrator
                'indd',               # Adobe InDesign
                'jp2', 'j2k'
            ]
            super().__init__(total_size,mime_type,image_extension)