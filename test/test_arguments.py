import unittest

from make import argparser as tm

class ParserTest(unittest.TestCase):
    def setUp(self):
        self.parser = tm.create_parser()

    def test_short(self):
        parsed = self.parser.parse_args(['-f', 'test'])
        self.assertEqual(parsed.file, 'test')

    def test_long(self):
        parsed = self.parser.parse_args(['-f', 'test'])
        self.assertEqual(parsed.file, 'test')

    def test_rule0(self):
        parsed = self.parser.parse_args([])
        self.assertEqual(parsed.rules, 'all')        

    def test_rule1(self):
        parsed = self.parser.parse_args(['a'])
        self.assertEqual(parsed.rules, ['a'])

    def test_rule3(self):
        parsed = self.parser.parse_args(['a','b','c'])
        self.assertEqual(parsed.rules, ['a','b','c'])



if __name__ == '__main__':
    unittest.main()