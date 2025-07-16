from src.categorizers.categories.category import Category
from src.enums.file_category import FileCategory


class ImageCategorizer(Category):
    def __init__(self):
            category_type:FileCategory = FileCategory.IMAGE
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
            super().__init__(total_size,mime_type,image_extension,category_type)