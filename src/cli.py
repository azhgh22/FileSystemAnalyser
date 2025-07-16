# This class is responsible for user interface. It read arguments for tool and runs it.
# arguments:
#           1. dir_path: str
#           2. follow_symlinks  [Y/n]
#           3. ignore_inaccessible_files [Y/n]
from src.categorizers.categories.executable_categorizer import ExecutableCategorizer
from src.categorizers.categories.image_categorizer import ImageCategorizer
from src.categorizers.categories.text_categorizer import TextCategorizer
from src.categorizers.categories.video_categorizer import VideoCategorizer
from src.categorizers.single_file_categorizer import SingleCategorizer
from src.file_permission_report.file_permission_report import FilePermissionReport
from src.large_file_identifier import LargeFileIdentifier
from src.service import Service
from src.traversals.standard_dir_traversal import StandardDirTraversal
from src.traversals.traversal import DirTraversal


class CLI:
    """Command-line interface for the FileSystemAnalyser tool."""
    def run(self) -> None:
        """Main loop to run the CLI tool, handle user input, and execute analysis."""
        while True:
            try:
                root_path, follow_symlinks, ignore_inaccessible_files, size_threshold = self.read_arguments()
                categorizer = SingleCategorizer(categories=[
                    TextCategorizer(),
                    ExecutableCategorizer(),
                    VideoCategorizer(),
                    ImageCategorizer()
                ])
                permission_reporter = FilePermissionReport()
                large_files_identifier = LargeFileIdentifier(size_threshold)

                traversal = StandardDirTraversal(root_path,follow_symlinks,ignore_inaccessible_files,services=[
                    categorizer,
                    permission_reporter,
                    large_files_identifier
                ])


                self.run_tool(traversal,categorizer,permission_reporter,large_files_identifier)
            except Exception as e:
                print(e)


            exit_from_tool = input("Exit [Y/n]: ").lower() == 'y'
            if exit_from_tool:
                break

        print("GoodBye")

    def read_arguments(self) -> tuple[str,str,str]:
        """Prompt the user for required arguments and validate them."""
        root_path = input('Enter root path: ')
        follow_symlinks = input('Follow symlinks [Y/n]: ').lower() == 'y'
        ignore_inaccessible_files = input('Ignore inaccessible files [Y/n]: ').lower() == 'y'
        large_file_threshold = input('enter size threshold for large files: ')

        try:
            large_file_threshold = int(large_file_threshold)
        except ValueError:
            raise ValueError('threshold must be number')

        return root_path, follow_symlinks, ignore_inaccessible_files,large_file_threshold

    def run_tool(self,  traversal:DirTraversal,
                        categorizer:Service,
                        permission_reporter:Service,
                        large_files_identifier:Service):
        """Run the directory traversal and generate all reports."""
        traversal.traverse()

        categorizer.make_report()
        permission_reporter.make_report()
        large_files_identifier.make_report()