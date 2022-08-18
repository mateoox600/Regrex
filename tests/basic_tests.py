import re
import unittest

from regrex import Regrex
from regrex_flag import RegrexFlag
from regrex_function import whitespace, word_char, combine, zero_or_more, one_or_more

class BasicTestCase(unittest.TestCase):

    def test_basic_regex(self):
        pattern = combine(zero_or_more(word_char()), one_or_more(whitespace()))
        regrex = Regrex(pattern, RegrexFlag.IGNORECASE | RegrexFlag.MULTILINE)

        self.assertIsInstance(regrex.match("testing "), re.Match)
        self.assertIsInstance(regrex.match(" "), re.Match)
        self.assertIsInstance(regrex.match("   "), re.Match)
        self.assertIsInstance(regrex.match("t "), re.Match)
        self.assertIsInstance(regrex.match("t   "), re.Match)
        self.assertIsInstance(regrex.match("test     "), re.Match)

        self.assertEqual(regrex.match("t"), None)
        self.assertEqual(regrex.match("testing"), None)
        self.assertEqual(regrex.match(""), None)

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
