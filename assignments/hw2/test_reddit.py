"""
HW 2: Scripting - Reddit testing

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

from reddit import build_parser, load_reddit_data, format_reddit_data

class RedditTestCases(unittest.TestCase):

    def test_build_parser(self):
        """tests the returned ArgumentParser from build_parser()"""
        parser = build_parser()

        # tests whether running the script with the help flag exits the script
        with self.assertRaises(SystemExit):
            parser.parse_args(['-h'])

        # test default values
        test_url = 'https://www.reddit.com/r/python/.json'
        args = parser.parse_args([test_url])
        self.assertEqual(args.url, test_url)
        self.assertEqual(args.n, 10)
        self.assertEqual(args.o, "score")
        self.assertEqual(args.t, 60)


    def test_load_reddit_data(self):
        """Tests the returned dict from load_reddit_data()."""
        raise NotImplementedError


    def test_format_reddit_data(self):
        """Tests the sorted and formatted list from format_reddit_data()."""
        raise NotImplementedError


if __name__ == "__main__":
    """Run your unit tests by python3 test_reddit.py"""
    unittest.main()