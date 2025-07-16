from enum import Enum

class FileCategory(str,Enum):
    """Enumeration of possible file categories."""
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    EXECUTABLE = "executable"
    UNDEFINED = "undefined"