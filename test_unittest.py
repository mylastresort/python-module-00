import unittest
from unittest.mock import patch
import ex01.exec as ex01
import ex02.whois as ex02
import ex03.count as ex03
import ex04.operations as ex04
import ex07.filterwords as ex07
import ex08.sos as ex08
import sys


class Test_Python_Module_00(unittest.TestCase):
    def test_ex01(self):
        testcases: list[tuple[list[str], str]] = [
            ([], ''),
            ([''], ''),
            (['', ''], ''),
            (['', '', ''], ''),
            (['    ', '   ', '   '], ''),
            (['Hello'], 'OLLEh'),
            (['Hello World!'], '!DLROw OLLEh'),
            (['Hello', 'my Friend'], 'DNEIRf YM OLLEh'),
            (['Hello', 'my        Friend'], 'DNEIRf YM OLLEh'),
            (['Hello      ', 'my        Friend'], 'DNEIRf YM OLLEh'),
            (['      Hello      ', '   my        Friend     '], 'DNEIRf YM OLLEh')
        ]
        for inp, out in testcases:
            ret = ex01.rev_alpha(inp)
            self.assertEqual(ret, out)

    def test_ex02(self):
        testcases = [
            (12, "I'm Even."),
            (3, "I'm Odd."),
            (0, "I'm Zero."),
            (-0, "I'm Zero."),
            (-12, "I'm Even."),
            (+12, "I'm Even."),
            (+11, "I'm Odd."),
            (+11, "I'm Odd."),
        ]
        for inp, out in testcases:
            ret = ex02.whois(inp)
            self.assertEqual(ret, out)

    @patch('builtins.print')
    def test_ex03(self, mock_print):
        testcases = [
            ("Python 2.0, released 2000, introduced \
features like List comprehensions and a garbage collection \
system capable of collecting reference cycles.",
             "The text contains 143 character(s):\n\
- 2 upper letter(s)\n\
- 113 lower letter(s)\n\
- 4 punctuation mark(s)\n\
- 18 space(s)"),
            ("Python is an interpreted, high-level, \
general-purpose programming language. Created by Guido van \
Rossum and first released in 1991, Python's design philosophy \
emphasizes code readability with its notable use of significant \
whitespace.", "The text contains 234 character(s):\n\
- 5 upper letter(s)\n\
- 187 lower letter(s)\n\
- 8 punctuation mark(s)\n\
- 30 space(s)"),
            ('Hello World!', "The text contains 12 character(s):\n\
- 2 upper letter(s)\n\
- 8 lower letter(s)\n\
- 1 punctuation mark(s)\n\
- 1 space(s)"),
        ]

        for inp, out in testcases:
            ex03.text_analyzer(inp)
            mock_print.assert_called_with(out)

        ex03.text_analyzer(42)
        mock_print.assert_called_with(
            'AssertionError: argument is not a string', file=sys.stderr)

        self.assertEqual(ex03.text_analyzer.__doc__, "\n\
    This function counts the number of upper characters, lower characters,\n\
    punctuation and spaces in a given text.")

    @patch('builtins.print')
    def test_ex04(self, mock_print):
        testcases = [
            ([10, 3], "Sum:\t\t13\n\
Difference:\t7\n\
Product:\t30\n\
Quotient:\t3.3333333333333335\n\
Remainder:\t1"),
            ([42, 10], "Sum:\t\t52\n\
Difference:\t32\n\
Product:\t420\n\
Quotient:\t4.2\n\
Remainder:\t2"),
            ([1, 0], "Sum:\t\t1\n\
Difference:\t1\n\
Product:\t0\n\
Quotient:\tERROR (division by zero)\n\
Remainder:\tERROR (modulo by zero)")
        ]

        for inp, out in testcases:
            ex04.operations(inp[0], inp[1])
            mock_print.assert_called_with(out)

    def test_ex07(self):
        testcases = [
            (['Hello, my friend', 3], ['Hello', 'friend']),
            (['Hello, my friend', 10], []),
            (['-A robot must protect its own existence as long as such protection does not \
conflict with the First or Second Law', 6], ['protect', 'existence', 'protection', 'conflict']),
        ]
        for inp, out in testcases:
            ret = ex07.filterwords(inp[0], inp[1])
            self.assertEqual(ret, out)

    def test_ex08(self):
        testcases = [
            (["SOS"], '... --- ...'),
            ([''], ''),
            (["96 BOULEVARD", "Bessiere"],
             '----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .'),
            (["96            BOULEVARD        ", " Bessiere        "],
             '----. -.... / -... --- ..- .-.. . ...- .- .-. -.. / -... . ... ... .. . .-. .'),
        ]

        for inp, out in testcases:
            ret = ex08.encode(ex08.join_args(inp))
            self.assertEqual(ret, out)


if __name__ == '__main__':
    unittest.main()
