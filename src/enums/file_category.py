from enum import Enum

class FileCategory(str,Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    EXECUTABLE = "executable"
    UNDEFINED = "undefined"