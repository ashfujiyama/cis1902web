"""Worksheet 1"""


def transpose(mat):
    """
    Task 1: transpose a given matrix.

    With zip() and either map() or a list comprehension, this can be
    implemented in one line!

    Args:
        mat (list): a list of lists representing a square matrix

    Returns:
        list: list representation of the matrix transpose
    """
    raise NotImplementedError


def evens_and_odds(n):
    """
    Task 2: Prints all pairs of numbers between 0 and n (exclusive) such that
    the first number is even and the second one is odd.

    Try implementing this with and without list comprehensions. What do you
    prefer in terms of readability?

    Args:
        n (int): the maximum number

    Returns:
        list: a list of tuples
    """
    raise NotImplementedError


"""
Task 3: course feedback
1. On a scale of 0 to 10, how have the lectures been so far?

2. What comments do you have for future lectures and assignments? What did you
like? What suggestions do you have for change?

3. What remaining questions do you have about the topics we have covered in the
course so far?

"""


if __name__ == '__main__':
    mat = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    print(transpose(mat))
    # expected: [[1, 4, 7], [2, 5, 8], [3, 6, 9]]

    print(evens_and_odds(5))
    # expected: [(0, 1), (0, 3), (2, 1), (2, 3), (4, 1), (4, 3)]