from __future__ import annotations
from re import Pattern, compile

def compile_regex(f):
    def wrapper(*args, **kwargs):
        return compile(f(*args, **kwargs))
    return wrapper

@compile_regex
def combine(*args: Pattern):
    return f"{''.join([pattern.pattern for pattern in args])}"

@compile_regex
def whitespace():
    return r"\s"

@compile_regex
def word_char():
    return r'\w'

@compile_regex
def many(pattern: Pattern):
    return f"{pattern.pattern}*"

@compile_regex
def many1(pattern: Pattern):
    return f"{pattern.pattern}+"