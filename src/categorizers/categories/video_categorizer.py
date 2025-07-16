from src.categorizers.categories.category import Category
from src.enums.file_category import FileCategory


class VideoCategorizer(Category):
    """Categorizes files as video based on extension and MIME type."""
    def __init__(self):
        """Initialize with video MIME types and extensions."""
        total_size:int = 0
        mime_type:list[str] = [
            "video/mp4",
            "video/x-m4v",
            "video/webm",
            "video/x-matroska",
            "video/x-flv",
            "video/dvd",
            "video/ogg",
            "video/x-msvideo",
            "video/quicktime",
            "video/x-ms-wmv",
            "video/mpeg",
            "video/3gpp",
            "video/3gpp2",
            "video/mp2t",
            "video/x-msvideo",  # for .avi
            "application/vnd.rn-realmedia",
            "application/vnd.rn-realmedia-vbr"
        ]
        image_extension:list[str] = [
            'mp4',  # MPEG-4
            'm4v',  # Apple variant of MP4
            'webm',  # WebM
            'mkv',  # Matroska
            'flv',  # Flash video
            'vob',  # DVD video
            'ogv',  # Ogg video
            'avi',  # AVI
            'mov',  # QuickTime
            'wmv',  # Windows Media Video
            'mpeg',  # MPEG
            'mpg',  # MPEG
            '3gp',  # 3GPP
            '3g2',  # 3GPP2
            'ts',  # MPEG Transport Stream
            'm2ts',  # Blu-ray video
            'rm',  # RealMedia
            'rmvb'  # RealMedia Variable Bitrate
        ]
        super().__init__(total_size,mime_type,image_extension,FileCategory.VIDEO)