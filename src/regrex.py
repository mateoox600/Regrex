from typing import Callable
from re import compile, Pattern

class Regrex:

    def __init__(self, pattern: Pattern, flags: int):
        self._pattern = pattern
        self._flags = flags
        self.compile_cache = None

    def compile(self, force=False):
        if force or self.compile_cache is None:
            self.compile_cache = compile(self._pattern.pattern, self._flags)
        return self.compile_cache

    def match(self, string: str):
        return self.compile().match(string)

    def set_pattern(self, new_pattern: Pattern):
        self._pattern = new_pattern
        self.compile_cache = None

    def set_flags(self, new_flags: int):
        self._flags = new_flags
        self.compile_cache = None

def regrex(f: Callable[..., tuple[Pattern, int]]):
    pattern, flag = f()
    return Regrex(pattern, flag)