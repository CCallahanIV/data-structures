"""This module implements a binary search tree."""

class Node(object):
    """Node object for use in a binary search tree."""
    def __init__(self):
        self.key = key
        self.value = value
        self.right = right
        self.left = left




class BinarySearchTree(object):
    """Binary Search Tree Object.

    Methods:
      - insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored.
      - search(self, val): will return the node containing that value, else None
      - size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.
      - depth(self): will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc.
      - contains(self, val): will return True if val is in the BST, False if not.
      - balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.

    """

    def __init__(self):
        """Initialize a Binary Search Tree object."""
        pass

    def insert(self, val):
      