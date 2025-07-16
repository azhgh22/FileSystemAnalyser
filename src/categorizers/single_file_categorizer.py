from dataclasses import dataclass, field

from src.categorizers.categories.category import Category
from src.enums.file_category import FileCategory
from src.file import File

@dataclass
class SingleCategorizer:
    categories:list[Category] = field(default_factory=lambda: [])

    def fit(self,file:File) -> File:
        for category in self.categories:
            new_file = category.categorize(file)
            if new_file.category != FileCategory.UNDEFINED:
                break

        return file

    def make_report(self) -> None:
        print('\n\nSize Analysis: ')
        for category in self.categories:
            print(category.category_type,' : ',category.total_size)

        print('\n')