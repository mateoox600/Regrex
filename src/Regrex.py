from re import compile, Pattern

class Regrex:

    def __init__(self, pattern: Pattern, flags: int):
        self.pattern = pattern
        self.flags = flags

    def compile(self):
        return compile(self.pattern.pattern, self.flags)