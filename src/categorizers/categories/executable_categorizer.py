from src.categorizers.categories.category import Category
from src.enums.file_category import FileCategory
from src.file import File


class ExecutableCategorizer(Category):
    def __init__(self):
        total_size:int = 0
        mime_type:list[str] = [
            "application/x-executable",
            "application/x-pie-executable",
            "application/x-mach-binary",
            "application/x-msdownload",
            "application/x-dosexec",
            "application/x-sharedlib",
            "application/x-object",
            "application/x-msdos-program",
            "application/octet-stream",  # fallback (use carefully)
            "application/x-exe"
        ]
        image_extension:list[str] = [
            # Windows
            ".exe", ".com", ".bat", ".cmd", ".msi", ".cpl", ".scr", ".hta", ".pif",
            ".vbs", ".vbe", ".js", ".jse", ".wsf", ".wsh", ".ps1", ".jar", ".gadget",
            ".lnk", ".msc",
            # macOS
            ".app", ".command", ".pkg", ".action", ".workflow", ".osx",
            # Linux/Unix-like
            ".sh", ".bin", ".run", ".out", ".pl", ".py", ".rb", ".csh", ".ksh"
        ]
        super().__init__(total_size,mime_type,image_extension,FileCategory.EXECUTABLE)