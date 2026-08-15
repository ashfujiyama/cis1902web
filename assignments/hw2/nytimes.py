#!/usr/bin/env python3
"""
HW 2: Scripting - New York Times

Name:

PennKey:

Number of hours spent on homework:
  - time spent on nytimes.py:
  - time spent on test_nytimes.py:

Collaboration is NOT permitted.

In all functions below, the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.

This assignment template was adapted from Peter Bui's Python scripting
assignment (c) 2020: https://gitlab.com/nd-cse-20289-sp20/cse-20289-sp20-assignments/
which is licensed under the MIT license agreement.
"""

import argparse # for parsing arguments
import json # for formatting and printing json
import requests # for making HTTP requests

def build_parser():
    """
    Builds an ArgumentParser with the specified parameters.

    Args:
        None

    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Pulls top articles from New York Times and displays them in terminal")
    # TODO implement the -n, -o, and -t flags
    raise NotImplementedError

    return parser


def load_data(section):
    """
    Load data from the specified url into a list of dicts.

    Don't forget to include your API key into the request URL.

    After correctly retrieving the response JSON dict from the NY Times API,
    you'll want the list of posts. It's up to you how you'd like to return
    the list of dict, so you need to think carefully about what portion of
    the JSON you need in order to implement format_data() and print_data().

    Hint: Use json.dumps(response.json(), indent=4) to print the response
    into a more readable format.

    Args:
        section (str): the chosen news category (arts, business, etc.)

    Returns:
        list: a list of dicts containing article information for the NY Times section.
    """
    raise NotImplementedError

def format_data(data, limit=10, order_by="title", title_len=60):
    """
    Sorts and formats the given NY Times data. If ordered by "time",
    make sure to sort descending order (most recent article first), and otherwise sort in
    ascending order.

    Hint: use an anonymous function to provide a key to list.sort()

    Args:
        data (list): a list of dicts containing the raw NY Times article data from
            load_data
        limit (int): the number of articles to return, default 10
        order_by (str): the attribute in the raw NY Times article data to sort by,
            default "title"
        title_len (int): the length of the title to show, default 60

    Returns:
        list: a list of dicts with with the following attributes in each dict:
            title (str): the possibly shortened article title
            time (str): the time of the article's publication (don't change the formatting
                from how you received it in the JSON response!)
            url (str): the url of the news article

    """
    raise NotImplementedError



def print_data(formatted_data):
    """
    Print NY Times data based on specified attributes using the following format:

      print("{index}.\t{title} (Date: {time})\n\t{url}\n".format(...))

    Note: you don't have to write unit tests for this function, and it will be
    ignored by the code coverage checker. We will be checking the output of
    your script against the solution however, so please follow the print format
    given above exactly!

    Args:
        formatted_data (list): a formatted list of articles returned from
            format_data()

    Returns:
        None
    """
    raise NotImplementedError

def main():
    """
    Builds an ArgumentParser object by calling build_parser(),
    loads the data from the given section by calling load_data(),
    and then prints the data using print_data().
    """
    parser = build_parser()
    # Parse command line arguments
    args = parser.parse_args()

    section = args.section
    limit     = args.n
    orderby   = args.o
    titlelen  = args.t

    # Load data from url and then print the data
    data = load_data(section)
    formatted_data = format_data(data, limit, orderby, titlelen)
    print_data(formatted_data)


if __name__ == '__main__':
    main()