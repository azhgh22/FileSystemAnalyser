from src.categorizers.categories.category import Category
from src.enums.file_category import FileCategory


class TextCategorizer(Category):
    def __init__(self):
        total_size:int = 0
        mime_type:list[str] = [
            "text/plain",
            "text/html",
            "text/css",
            "text/csv",
            "text/tab-separated-values",
            "text/xml",
            "text/markdown",
            "text/x-rst",
            "text/x-python",
            "text/x-csrc",
            "text/x-c++src",
            "text/x-java-source",
            "text/x-shellscript",
            "text/x-sql",
            "text/x-tex",
            "text/x-ini",
            "text/x-log",
            "text/x-yaml",
            "text/x-makefile",
            "text/x-perl",
            "text/x-kotlin",
            "text/x-go",
            "text/x-lua",
            "text/x-ruby",
            "text/x-pascal",
            "text/x-php",
            "text/x-tcl",
            "text/x-fortran",
            "text/x-asm",
            "text/x-bibtex",
            "text/x-markdown",
            "text/x-properties"
        ]
        image_extension:list[str] = [
            'txt', 'csv', 'tsv', 'log', 'md', 'rst', 'json', 'xml',
            'yaml', 'yml', 'ini', 'conf', 'py', 'c', 'cpp', 'java',
            'html', 'htm', 'css', 'js', 'sql', 'tex'
        ]
        super().__init__(total_size,mime_type,image_extension,FileCategory.TEXT)