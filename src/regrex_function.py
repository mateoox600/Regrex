from __future__ import annotations

import re
from re import Pattern, compile

def compile_regex(f):
    def wrapper(*args, **kwargs):
        return compile(f(*args, **kwargs))
    return wrapper

@compile_regex
def any_char():
    return r"."

@compile_regex
def whitespace():
    return r"\s"

@compile_regex
def non_whitespace():
    return r"\S"

@compile_regex
def digit():
    return r"\d"

@compile_regex
def non_digit():
    return r"\D"

@compile_regex
def word_char():
    return r'\w'

@compile_regex
def non_word_char():
    return r"\D"

@compile_regex
def vertical_whitespace():
    return r"v"

@compile_regex
def literal(string: str):
    return re.escape(string)

@compile_regex
def string_start():
    return r"^"

@compile_regex
def string_end():
    return r"$"

@compile_regex
def word_boundary():
    return "\b"

@compile_regex
def non_word_boundary():
    return "\B"

@compile_regex
def choice(*args: Pattern):
    return f"({'|'.join([pattern.pattern for pattern in args])})"

@compile_regex
def combine(*args: Pattern):
    return f"({''.join([pattern.pattern for pattern in args])})"

@compile_regex
def zero_or_more(pattern: Pattern):
    return f"({pattern.pattern})*"

@compile_regex
def one_or_more(pattern: Pattern):
    return f"({pattern.pattern})+"

@compile_regex
def lazy(pattern: Pattern):
    return f"({pattern.pattern})*?"

@compile_regex
def optional(pattern: Pattern):
    return f"({pattern})?"

@compile_regex
def repeat(pattern: Pattern, times: int):
    return f"({pattern}{{{times}}})"

@compile_regex
def repeat_or_more(pattern: Pattern, times: int):
    return f"({pattern}{{{times},}})"

@compile_regex
def repeat_between(pattern: Pattern, min_times: int, max_times: int):
    return f"({pattern}{{{min_times},{max_times}}})"