from __future__ import annotations
from enum import IntEnum

class RegrexFlag(IntEnum):
    TEMPLATE = 1 << 0
    IGNORECASE = 1 << 1
    LOCALE = 1 << 2
    MULTILINE = 1 << 3
    DOTALL = 1 << 4
    UNICODE = 1 << 5
    VERBOSE = 1 << 6
    DEBUG = 1 << 7
    ASCII = 1 << 8
