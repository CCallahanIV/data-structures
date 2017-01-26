"""A trie data structure implemented as a class."""

from collections import OrderedDict


class Node(object):
    """Node object to build a trie."""

    def __init__(self, prev=None, end=False):
        """Init node object."""
        self.prev = prev
        self.children = OrderedDict()
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

    @property
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
        if curr_node.end and not curr_node.children:
            i = 1
            while curr_node.prev is not self.root and not curr_node.prev.end and len(curr_node.prev.children) < 2:
                curr_node = curr_node.prev
                i += 1
            del curr_node.prev.children[string[-i]]
            curr_node.prev = None
        else:
            curr_node.end = False
        self._size -= 1

    def __len__(self):
        """Allow use of len() function."""
        return self.size()

    def traversal(self, start=None):
        """Return a generator containing complete tokens (words) from a starting point."""
        start_node = self.root
        if start is not None:
            for char in start:
                if char in start_node.children:
                    start_node = start_node.children[char]
                else:
                    raise ValueError("That string is not in this Trie.")

        trav_list = []
        for i, (key, node) in enumerate(start_node.children.items()):
            trav_list.append((key, node))

        while trav_list:
            curr = trav_list.pop()
            yield curr[0]

            for key, node in curr[1].children:
                trav_list.append(key, node)
