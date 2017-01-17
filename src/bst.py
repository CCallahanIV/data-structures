"""This module implements a binary search tree."""


class Node(object):
    """Node object for use in a binary search tree."""

    def __init__(self, value, right=None, left=None):
        self.value = value
        self.right = right
        self.left = left

    def _has_children(self):
        """Return True or False if Node has children."""
        if self.right or self.left:
            return True
        return False


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
        self.root = None
        self.size = 0

    def insert(self, val):
        """Insert a new node with val into the BST."""
        # if not self.search(val):
        #     return
        new_node = Node(val)
        if self.root is None:
            self.root = new_node
            self.size = 1
            return

        curr_node = self.root
        while curr_node:
            if val > curr_node.value:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = new_node
                    self.size += 1
                    break
            elif val < curr_node.value:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = new_node
                    self.size += 1
                    break
            else:
                break

    def search(self, val):
        """Return the node with value val or return None."""
        pass

    def size(self):
        """Return the integer size of the BST."""
        return self.size

    def depth(self, start=None):
        """Return the integer depth of the BST."""
        def depth_wrapped(start):
            if start is None:
                return 0
            else:
                return max(depth_wrapped(start.right), depth_wrapped(start.left)) + 1
        if start is None:
            return depth_wrapped(self.root)
        else:
            return depth_wrapped(start)

    def contains(self, val):
        """Return True if node with value val is in BST, False if not."""
        pass

    def balance(self):
        """Return positive or negative integer that represents how well balanced the tree is."""
        if self.root is None:
            return 0
        return self.depth(self.root.right) - self.depth(self.root.left)
