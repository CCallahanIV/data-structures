"""Module for Binary Search Tree."""


class BinarySearchTree(object):
    """Foo."""

    def __init__(self):
        """Init of the Binary Search Tree class."""
        self._bstdict = {}
        self.root = None
        self.vertex = self.root

    def insert(self, val):
        """Takes a value, inserts into Binary Search Tree at correct placement."""
        if not any(self._bstdict):
            self.root = val
            self._bstdict[val] = ["z", "z"]

        elif val > self._bstdict[self.vertex]:
            if self._bstdict[self.vertex][1] == "z":
                self._bstdict[self.vertex][1] = val
            self.vertex = self.vertex[1]
            insert(val)

        elif val < self._bstdict[self.vertex]:
            if self._bstdict[self.vertex][0] == "z":
                self._bstdict[self.vertex][0] = val
            self.vertex = self.vertex[0]
            insert(val)
