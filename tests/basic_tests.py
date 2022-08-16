import re
import unittest

from Regrex import Regrex
from RegrexFlag import RegrexFlag
from RegrexFunction import whitespace, word_char, combine, many, many1

class MyTestCase(unittest.TestCase):
    def test_basic_regex(self):
        pattern = combine(many(word_char()), many1(whitespace()))
        regrex = Regrex(pattern, RegrexFlag.IGNORECASE | RegrexFlag.MULTILINE)
        regex = regrex.compile()

        self.assertIsInstance(regex.match("testing "), re.Match)
        self.assertIsInstance(regex.match(" "), re.Match)
        self.assertIsInstance(regex.match("t "), re.Match)
        self.assertIsInstance(regex.match("t   "), re.Match)
        self.assertIsInstance(regex.match("ttest     "), re.Match)

        self.assertEqual(regex.match("t"), None)
        self.assertEqual(regex.match("tsdgfg"), None)

if __name__ == '__main__':
    unittest.main()
