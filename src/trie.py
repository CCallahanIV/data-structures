

"""
    insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.
    contains(self, string): will return True if the string is in the trie, False if not.
    size(self): will return the total number of words contained within the trie. 0 if empty.
    remove(self, string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception.
"""

class Node(object):
    """Node class."""

    def __init__(self, value=None, left=None, right=None):
        """Init of the Node class."""
        self.value = value
        self.node = node
        self.right = right
        self.parent = None
