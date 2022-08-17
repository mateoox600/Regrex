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
        self.assertIsInstance(regex.match("t "), re.Match)
        self.assertIsInstance(regex.match("t   "), re.Match)
        self.assertIsInstance(regex.match("ttest     "), re.Match)

        self.assertEqual(regex.match("t"), None)
        self.assertEqual(regex.match("tsdgfg"), None)
        self.assertEqual(regex.match(""), None)

if __name__ == '__main__':
    unittest.main()
