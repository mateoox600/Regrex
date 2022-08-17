import re
import unittest

from regrex import Regrex
from regrex_flag import RegrexFlag
from regrex_function import whitespace, word_char, combine, zero_or_more, one_or_more

class BasicTestCase(unittest.TestCase):

    def test_basic_regex(self):
        pattern = combine(zero_or_more(word_char()), one_or_more(whitespace()))
        regrex = Regrex(pattern, RegrexFlag.IGNORECASE | RegrexFlag.MULTILINE)
        regex = regrex.compile()

        self.assertIsInstance(regex.match("testing "), re.Match)
        self.assertIsInstance(regex.match(" "), re.Match)
        self.assertIsInstance(regex.match("   "), re.Match)
        self.assertIsInstance(regex.match("t "), re.Match)
        self.assertIsInstance(regex.match("t   "), re.Match)
        self.assertIsInstance(regex.match("test     "), re.Match)

        self.assertEqual(regex.match("t"), None)
        self.assertEqual(regex.match("testing"), None)
        self.assertEqual(regex.match(""), None)

    def test_basic_flag_to_string_uses(self):
        empty_flag = RegrexFlag.to_flags_string(0)
        ignore_multiline_flag = RegrexFlag.to_flags_string(RegrexFlag.IGNORECASE | RegrexFlag.MULTILINE)
        multiple_flag_out_of_order = RegrexFlag.to_flags_string(
            RegrexFlag.IGNORECASE | RegrexFlag.MULTILINE | RegrexFlag.ASCII | RegrexFlag.LOCALE
        )

        self.assertEqual(empty_flag, "")
        self.assertEqual(ignore_multiline_flag, "im")
        self.assertEqual(multiple_flag_out_of_order, "ilma")

if __name__ == '__main__':
    unittest.main()
