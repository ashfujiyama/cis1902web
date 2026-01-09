#!/usr/bin/env python3
"""
HW 2: Scripting - Reddit

Name:

PennKey:

Number of hours spent on homework:

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

# Global constant for URL shortener website
ISGD_URL = 'http://is.gd/create.php'

def build_parser():
    """
    Builds an ArgumentParser with the specified parameters.

    Args:
        None

    Returns:
        argparse.ArgumentParser
    """
    parser = argparse.ArgumentParser(description="Pulls top posts from subreddit and displays them in terminal")
    parser.add_argument('url', help="the URL or subreddit to visit")

    # TODO implement the -n, -o, and -t flags
    raise NotImplementedError

    return parser


def load_reddit_data(url):
    """
    Load reddit data from the specified url into a list of dicts.

    You'll need to verify the url parameter. If it starts with http, then
    use it, otherwise assume it is a subreddit.

    Make sure to use the headers specified in the homework description when
    making your get requests!

    After correctly retrieving the response JSON dict from reddit, you'll want
    the list of posts. It's up to you how you'd like to return the list of
    dict, so you need to think carefully about what portion of the JSON you
    need in order to implement format_reddit_data() and print_reddit_data().

    Hint: Use json.dumps(response.json(), indent=4) to print the response
    into a more readable format.

    We don't require any error handling for non-existent subreddits or malformed
    URLs, but you are welcome to optionally do so.

    Args:
        url (str): the url (or subreddit)

    Returns:
        list: a list of dicts containing post information for the subreddit.
    """
    raise NotImplementedError


def format_reddit_data(data, limit=10, order_by="score", title_len=60):
    """
    Sorts and formats the given reddit data. If ordered by "score",
    make sure to sort in descending order, otherwise sort in ascending order.

    Hint: use an anonymous function to provide a key to list.sort()

    Args:
        data (list): a list of dicts containing the raw reddit post data from
            load_reddit_data
        limit (int): the number of posts to return, default 10
        order_by (str): the attribute in the raw reddit post data to sort by,
            default "score"
        title_len (int): the length of the title to show, default 60

    Returns:
        list: a list of dicts with with the following attributes in each dict:
            title (str): the possibly shortened post title
            score (str): the score of the post
            url (str): the url to the post
    """
    raise NotImplementedError


def print_reddit_data(formatted_data):
    """
    Print reddit data based on specified attributes using the following format:

      print("{index}.\t{title} (Score: {score})\n\t{url}".format(...))

    Note: you don't have to write unit tests for this function, and it will be
    ignored by the code coverage checker. We will be checking the output of
    your script against the solution however, so please follow the print format
    given above exactly!

    Args:
        formatted_data (list): a formatted list of posts returned from
            format_reddit_data()

    Returns:
        None
    """
    raise NotImplementedError

def shorten_url(url):
    """
    Shortens the given url using is.gd service.

    Args:
        url (str): the url to shorten

    Returns:
        str: the shortened url

    Examples:

    >>> shorten_url('https://reddit.com/r/cats')
    'https://is.gd/0bLK0t'

    >>> shorten_url('https://www.cis.upenn.edu/~cis1920/tliu/')
    'https://is.gd/aqBtxQ'
    """
    r = requests.get(ISGD_URL, params={'format': 'json', 'url': url})
    response = r.json()
    return response['shorturl']

def main():
    """
    Builds an ArgumentParser object by calling build_parser(),
    loads the data from the given URL by calling load_reddit_data(),
    and then prints the data using print_reddit_data().
    """
    parser = build_parser()
    # Parse command line arguments
    args = parser.parse_args()

    url = args.url
    limit     = args.n
    orderby   = args.o
    titlelen  = args.t

    # Load data from url and then print the data
    data = load_reddit_data(url)
    formatted_data = format_reddit_data(data, limit, orderby, titlelen)
    print_reddit_data(formatted_data)


if __name__ == '__main__':
    """
    example code for getting headers, also in the hw description
    headers = {
    "user-agent": "CIS 1920 Spring 2023 HW3 by [insert your email here]"
    }
    response = requests.get("https://www.reddit.com/r/python/.json", headers=headers)
    print(json.dumps(response.json(), indent=4))
    """
    main()