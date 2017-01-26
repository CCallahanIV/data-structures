"""A trie data structure implemented as a class."""


class Node(object):
    """Node object to build a trie."""

    def __init__(self, prev=None, end=False):
        """Init node object."""
        self.prev = prev
        self.children = {}
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
        self._size = 0

    def insert(self, string):
        """Insert string into the trie."""
        current_node = self.root
        for i in range(len(string)):
            if string[i] not in current_node.children:
                new_node = Node(prev=current_node)
                current_node.children[string[i]] = new_node
            current_node = current_node.children[string[i]]
        current_node.end = True
        self._size += 1

    def contains(self, string):
        """Return a boolean, true if the string is present, else false."""
        curr_node = self.root
        for char in string:
            if char in curr_node.children:
                curr_node = curr_node.children[char]
            else:
                return False
        return curr_node.end

    def size(self):
        """Return the number of strings in the trie."""
        return self._size

    def remove(self, string):
        """Remove a string from the trie. Exception if string is absent."""
        curr_node = self.root
        for i in range(len(string)):
            if string[i] in curr_node.children:
                curr_node = curr_node.children[string[i]]
            else:
                raise ValueError("That word is not in this Trie.")
        if curr_node.children[string[-1]].end and not curr_node.children[string[-1]].children:
            i = 1
            while curr_node.prev is not self.root or not curr_node.prev.end:
                curr_node = curr_node.prev
                i += 1
            del curr_node.prev.children[string[-i]]
            curr_node.prev = None
        else:
            curr_node.children[string[-1]].end = False
        self._size -= 1

    def __len__(self):
        """Allow use of len() function."""
        return self.size()
