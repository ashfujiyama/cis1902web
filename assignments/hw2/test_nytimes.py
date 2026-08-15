"""
HW 2: Scripting - New York Times testing

Collaboration is NOT permitted.

In all functions below, the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.

This assignment template was adapted from Peter Bui (c) 2020's Python scripting
assignment: https://gitlab.com/nd-cse-20289-sp20/cse-20289-sp20-assignments/
which is licensed under the MIT license agreement.
"""

import unittest

from nytimes import build_parser, load_data, format_data

class NYTTestCases(unittest.TestCase):

    def test_build_parser(self):
        """tests the returned ArgumentParser from build_parser()"""
        parser = build_parser()

        # tests whether running the script with the help flag exits the script
        with self.assertRaises(SystemExit):
            parser.parse_args(['-h'])

        # test default values
        test_section = 'home'
        args = parser.parse_args([test_section])
        self.assertEqual(args.section, test_section)
        self.assertEqual(args.n, 10)
        self.assertEqual(args.o, "title")
        self.assertEqual(args.t, 60)


    def test_load_data(self):
        """Tests the returned dict from load_data()."""
        raise NotImplementedError


    def test_format_data(self):
        """Tests the sorted and formatted list from format_data()."""
        raise NotImplementedError


if __name__ == "__main__":
    """Run your unit tests by python3 test_nytimes.py"""
    unittest.main()