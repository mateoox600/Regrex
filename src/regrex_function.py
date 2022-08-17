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
def char_from_hex(number: int):
    return f'\\x{hex(number).lstrip("0x")}'

@compile_regex
def char_from_code(code: int):
    return f'\\x{code}'

@compile_regex
def one_char_of(string: str):
    return f'[{string}]'

@compile_regex
def any_char_exept(string: str):
    return f'[^{string}]'

@compile_regex
def char_in_range(ranges: list[tuple[str, str]]):
    return f'[{"".join([f"{range[0]}-{range[1]}" for range in ranges])}]'

@compile_regex
def char_outside_range(ranges: list[tuple[str, str]]):
    return f'[^{"".join([f"{range[0]}-{range[1]}" for range in ranges])}]'

@compile_regex
def new_line():
    return r"\n"

@compile_regex
def carriage_return():
    return r"\r"

@compile_regex
def tab():
    return r"\t"

@compile_regex
def null_char():
    return r"\0"

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
def backspace_char():
    return r"[\b]"

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
    return r"\b"

@compile_regex
def non_word_boundary():
    return r"\B"

@compile_regex
def sub_pattern_match_number(group_number: int):
    return f'\\{group_number}'

@compile_regex
def choice(*args: Pattern):
    return f"(?:{'|'.join([pattern.pattern for pattern in args])})"

@compile_regex
def combine(*args: Pattern):
    return f"(?:{''.join([pattern.pattern for pattern in args])})"

@compile_regex
def zero_or_more(pattern: Pattern):
    return f"(?:{pattern.pattern})*"

@compile_regex
def one_or_more(pattern: Pattern):
    return f"(?:{pattern.pattern})+"

@compile_regex
def lazy(pattern: Pattern):
    return f"(?:{pattern.pattern})*?"

@compile_regex
def optional(pattern: Pattern):
    return f"(?:{pattern.pattern})?"

@compile_regex
def repeat(pattern: Pattern, times: int):
    return f"(?:{pattern.pattern}{{{times}}})"

@compile_regex
def repeat_or_more(pattern: Pattern, times: int):
    return f"(?:{pattern.pattern}{{{times},}})"

@compile_regex
def repeat_between(pattern: Pattern, min_times: int, max_times: int):
    return f"(?:{pattern.pattern}{{{min_times},{max_times}}})"

@compile_regex
def group(pattern: Pattern):
    return f"({pattern.pattern})"

@compile_regex
def named_group(name: str, pattern: Pattern):
    return f"(?P<{name}>{pattern.pattern})"

# TODO: parse flags and add them to inline flags block
@compile_regex
def inline_flags(flags: int):
    return f"(?)"

# TODO: parse flags and add them to localized flags block
@compile_regex
def localized_inline_flags(flags: int, pattern: Pattern):
    return f"(?flags:{pattern.pattern})"

@compile_regex
def conditional_pattern(group: int, true_pattern: Pattern, false_pattern: Pattern):
    return f"(?({group}){true_pattern.pattern}|{false_pattern.pattern})"

@compile_regex
def sub_pattern_match_name(group_name: str):
    return f'(?P={group_name})'

@compile_regex
def positive_lookahead(pattern: Pattern):
    return f'(?={pattern.pattern})'

@compile_regex
def negative_lookahead(pattern: Pattern):
    return f'(?!{pattern.pattern})'

@compile_regex
def positive_lookbehind(pattern: Pattern):
    return f'(?<={pattern.pattern})'

@compile_regex
def negative_lookbehind(pattern: Pattern):
    return f'(?<!{pattern.pattern})'

