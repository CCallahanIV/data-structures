"""Module for Binary Search Tree."""


class Node(object):

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    

class BinarySearchTree(object):
    """Foo."""

    """insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored."""
    """search(self, val): will return the node containing that value, else None"""
    """size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty."""
    """depth(self): will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc."""
    """contains(self, val): will return True if val is in the BST, False if not."""
    """balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0."""


    def __init__(self):
        """Init of the Binary Search Tree class."""
        self.root = None
        self.counter = 0

    def insert(self, val):
        """Takes a value, inserts into Binary Search Tree at correct placement."""
        if self.root is None:
            self.root = Node(val)
            self.counter += 1

        else:
            vertex = self.root
            while True:
                if val > vertex.value:
                    if vertex.right:
                        vertex = vertex.right
                    else:
                        vertex.right = Node(val)
                        self.counter += 1
                        break

                elif val < vertex.value:
                    if vertex.left:
                        vertex = vertex.left
                    else:
                        vertex.left = Node(val)
                        self.counter += 1
                        break


    # def search(self, val):


    def size(self):
        """Returns size of Binary Search Tree."""
        
