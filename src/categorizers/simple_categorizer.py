from dataclasses import dataclass, field

from src.categorizers.categories.category import Category
from src.enums.file_category import FileCategory
from src.file import File

@dataclass
class SimpleCategorizer:
    categories:list[Category] = field(default_factory=lambda: [])

    def categorize(self,files:list[File]) -> list[File]:
        categorize_files = []
        for file in files:
            for category in self.categories:
                new_file = category.categorize(file)
                if new_file.category != FileCategory.UNDEFINED:
                    categorize_files.append(new_file)
                    break

        return categorize_files