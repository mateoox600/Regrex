from typing import Callable
from re import compile, Pattern

class Regrex:

    def __init__(self, pattern: Pattern, flags: int):
        self.pattern = pattern
        self.flags = flags
        self.compile_cache = None

    def compile(self, force=False):
        if force or self.compile_cache is None:
            self.compile_cache = compile(self.pattern.pattern, self.flags)
        return self.compile_cache

    def match(self, string: str):
        return self.compile().match(string)

def regrex(f: Callable[..., tuple[Pattern, int]]):
    pattern, flag = f()
    return Regrex(pattern, flag)