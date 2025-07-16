from dataclasses import dataclass, field

from src.categorizers.categories.category import Category
from src.enums.file_category import FileCategory
from src.file import File

@dataclass
class SingleCategorizer:
    """Categorizes files into a single category using a list of Category objects."""
    categories:list[Category] = field(default_factory=lambda: [])

    def fit(self,file:File) -> File:
        """Categorize the file using the available categories."""
        for category in self.categories:
            new_file = category.categorize(file)
            if new_file.category != FileCategory.UNDEFINED:
                break

        return file

    def make_report(self) -> None:
        """Print a report of the total size for each category."""
        print('\n\nSize Analysis: ')
        for category in self.categories:
            print(category.category_type,' : ',category.total_size)

        print('\n')