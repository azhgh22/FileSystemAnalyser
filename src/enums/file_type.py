from enum import Enum

class FileType(str,Enum):
    DIR = 'directory'
    FILE = 'file'
    NONE = 'none'
