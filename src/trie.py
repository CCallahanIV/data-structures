"""A trie data structure implemented as a class."""


class Node(object):
    """Node object to build a trie."""

    def __init__(self, prev=None, children={}, end=False):
        """Init node object."""
        self.prev = prev
        self. children = children
        self.end = end


class Trie(object):
    """
    Trie class.

    __init__:
    insert(string): adds a string to the trie.
    contains(string): returns true if string is in the trie, else false.
    size(): returns the number of words in the trie. 0 if empty.
    remove(string): will remove the string from the trie. Exception otherwise.
    """

    def __init__(self):
        """Initialize the Trie class."""
        self.root = Node()
        self.size = 0

    def insert(self, string):
        """Insert string into the trie."""
        current_node = self.root
        for i in range(len(string)):
            if string[i] in current_node.children:
                current_node.children.setdefault(string[i], Node(prev=current_node))
            current_node = current_node.children[string[i]]
        current_node.end = True
        self.size += 1

    def contains(self, string):
        """Return a boolean, true if the string is present, else false."""
        pass

    def size(self):
        """Return the number of strings in the trie."""
        pass

    def remove(self, string):
        """Remove a string from the trie. Exception if string is absent."""
        pass
