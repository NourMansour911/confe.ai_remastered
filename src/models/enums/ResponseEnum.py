from enum import Enum

class ResponseEnum(Enum):
    FILE_SIZE_EXCEEDED = "File Size Exceeded"
    FILE_TYPE_NOT_ALLOWED = "File Type Not Allowed"
    FILE_VALID = "File Validated Successfully"
    FILE_INVALID = "File Invalid"

