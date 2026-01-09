"""
HW 1: BSTs

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


class Node:
    def __init__(self, key):
        """
        Construct an instance of the Node class.

        Attributes:
            - self.key: the int representing the key for the node
            - self.left: the left child Node object (initialize to None)
            - self.right: the right child Node object (initialize to None)

        Args:
            key (int): the key for the node
        """
        raise NotImplementedError

    def insert(self, key):
        """
        Inserts the given key, and raises an Exception if the key already
        exists.

        Args:
            key (int): the key for the node

        Returns:
            None

        Raises:
            Exception: if the key already exists.
        """
        raise NotImplementedError

    def search(self, key):
        """
        Searches for the given key, and returns the Node the key
        is at, if it exists.

        Args:
            key (int): the key to be inserted

        Returns:
            Node: the node that contains the given key, or None if not found
        """
        raise NotImplementedError

    def __str__(self):
        """
        Defines the string representation of a given Node instance.

        This function is optional and won't be graded, but you may find it
        useful to print Node attributes for debugging.

        Args:
            None

        Returns:
            str: a Node's string representation
        """
        raise NotImplementedError


class BST:
    def __init__(self):
        """
        Construct an instance of the BST class. The BST should be initially
        empty.

        Attributes:
            - self.root: root Node of the BST (initialize to None)
            - self.length (initialize to 0)
        """
        raise NotImplementedError

    def insert(self, key):
        """
        Insert a node to the BST with a given key.

        Wraps the Node insert() function, but should catch the Exception
        raised by Node.insert() if a duplicate key is inserted.

        Remember to increment self.length when an insert is successful.

        Args:
            key (int): the key to insert in the BST

        Returns:
            bool: True if the key is successfully inserted, False if it is
            a duplicate.
        """
        raise NotImplementedError

    def __len__(self):
        """
        The number of elements in the BST.

        Args:
            None

        Return:
            int: the number of elements in the BST
        """
        raise NotImplementedError

    def search(self, key):
        """
        Searches for the given key, and returns the Node the key
        is at, if it exists.

        Wraps the Node search() function.

        Args:
            key (int): the key to search for in the BST

        Returns:
            Node: the node with the given key if present, None otherwise
        """
        raise NotImplementedError

    def __contains__(self, key):
        """
        Check whether the given key is in the BST.

        Hint: use your implemented search function.

        Args:
            key (int): the key to search for

        Returns:
            True if the key is in the BST, False otherwise
        """
        raise NotImplementedError

    def __iter__(self):
        """
        A generator for iterating over the keys of the tree, in an in-order
        traversal.

        Hint: consider writing a recursive helper function, using yield and
        yield from.

        Args:
            None

        Yields:
            Keys of the BST in-order
        """
        raise NotImplementedError


if __name__ == '__main__':
    """
    Feel free to test your implementation here by running "python3 hw2.py" in
    your terminal.
    """
    my_bst = BST()