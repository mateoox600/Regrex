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

    @staticmethod
    def to_flags_string(flag: int):
        flag_string = ""
        for regrex_flag in RegrexFlag:
            if flag & regrex_flag != 0:
                flag_string += FLAGS_CHAR_MAP[regrex_flag]
        return flag_string

# a map for all char flags
FLAGS_CHAR_MAP = {
    RegrexFlag.IGNORECASE: 'i',
    RegrexFlag.LOCALE: 'l',
    RegrexFlag.MULTILINE: 'm',
    RegrexFlag.DOTALL: 's',
    RegrexFlag.VERBOSE: 'x',
    RegrexFlag.ASCII: 'a'
}