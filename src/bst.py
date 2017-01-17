"""This module implements a binary search tree."""

from queue_ds import Queue


class Node(object):
    """Node object for use in a binary search tree."""

    def __init__(self, value, right=None, left=None):
        """Initialize a node for a binary search tree object."""
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
      - in_order(self): will return a generator that will return the values in the tree using in-order traversal, one at a time.
      - pre_order(self): will return a generator that will return the values in the tree using pre-order traversal, one at a time.
      - post_order(self): will return a generator that will return the values in the tree using post_order traversal, one at a time.
      - breadth_first(self): will return a generator that will return the values in the tree using breadth-first traversal, one at a time.

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
        start = self.root
        while True:
            if start.value == val:
                return start
            elif val < start.value and start.left:
                start = start.left
            elif val > start.value and start.right:
                start = start.right
            else:
                return None

    def size(self):
        """Return the integer size of the BST."""
        return self.size

    def __len__(self):
        """Return integer size of the BST."""
        return self.size()

    def depth(self, start=''):
        """Return the integer depth of the BST."""
        def depth_wrapped(start):
            if start is None:
                return 0
            else:
                return max(depth_wrapped(start.right), depth_wrapped(start.left)) + 1
        if start is '':
            return depth_wrapped(self.root)
        else:
            return depth_wrapped(start)

    def contains(self, val):
        """Return True if node with value val is in BST, False if not."""
        try:
            return self.search(val).value == val
        except AttributeError:
            return False

    def balance(self):
        """Return positive or negative integer that represents how well balanced the tree is."""
        if self.root is None:
            return 0
        return self.depth(self.root.right) - self.depth(self.root.left)

    def in_order(self):
        """Return a generator of the tree in in_order order."""
        pass

    def pre_order(self):
        """Return a generator of the tree in pre_order order."""
        pass

    def post_order(self):
        """Return a generator of the tree in post_order order."""
        pass

    def breadth_first(self):
        """Return a generator of the tree in breadth first traversal order."""
        start = self.root
        q = Queue()
        q.enqueue(start)

        while len(q) > 0:
            current = q.dequeue()
            if current not in path:
                path.append(current)

            for neighbor in self._gdict[current]:
                if neighbor not in path:
                    q.enqueue(neighbor)
