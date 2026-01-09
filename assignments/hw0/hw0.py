"""
HW 1: Tries

Name:

PennKey:

Number of hours spent on homework:

Collaboration is NOT permitted.

In all functions below, the "NotImplementedError" exception is raised, for
you to fill in. The interpreter will not consider the empty code blocks
as syntax errors, but the "NotImplementedError" will be raised if you
call the function. You will replace these raised exceptions with your
code completing the function as described in the docstrings.
"""


def add_word(trie, word):
    """
    Add a word to the given trie.

    Args:
        trie (dict): the dictionary representation of a trie
        word (str): the word to be added

    Returns:
        None

    Side effect:
        trie is modified with word included
    """
    raise NotImplementedError


def create_trie(word_list):
    """
    Creates a trie from the given word list.

    Hint: use your completed implementation of add_word()

    Args:
        word_list (list): list of words (str)

    Returns:
        dict: a dictionary representation of the trie
    """
    raise NotImplementedError


def in_trie(trie, word):
    """
    Check whether the given word is present within the trie.

    Args:
        word (str): the word to check
        trie (dict): the trie to check against

    Returns:
        bool: True if the word is in the trie, False if it is not
    """
    raise NotImplementedError


def list_matches(trie, prefix):
    """
    List all word with the given prefix in the trie.
    If no words in the trie match the given prefix, return an empty list.

    Hint: you may want to write a recursive helper function to traverse the
    trie.

    Args:
        prefix (str): the prefix to match against
        trie (dict): the trie to search over

    Returns:
        list: all words in the trie that begin with prefix
    """
    raise NotImplementedError


def main():
    """main function"""
    word_list = ['bear']
    my_trie = create_trie(word_list)
    print(my_trie)


if __name__ == '__main__':
    """
    Feel free to test your implementation here by running python3 hw1.py in
    your terminal
    """
    main()