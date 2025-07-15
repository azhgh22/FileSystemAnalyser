from enum import Enum

class FileCategory(str,Enum):
    TEXT = "text"
    IMAGE = "image"
    VIDEO = "video"
    AUDIO = "audio"
    EXECUTABLE = "executable"
    ARCHIVE = "archive"
    PDF = "pdf"
    OTHER = "other"