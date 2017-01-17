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
        import pdb; pdb.set_trace()
        if not any(self._bstdict):
            self.root = val
            self._bstdict[val] = [None, None]

        elif val > self._bstdict[self.vertex]:
            if self._bstdict[self.vertex][1] == None:
                self._bstdict[self.vertex][1] = val
            self.vertex = self.vertex[1]
            insert(val)

        elif val < self._bstdict[self.vertex]:
            if self._bstdict[self.vertex][0] == None:
                self._bstdict[self.vertex][0] = val
            self.vertex = self.vertex[0]
            insert(val)
