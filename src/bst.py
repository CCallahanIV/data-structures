"""Module for Binary Search Tree."""

from queue_ds import Queue


class Node(object):
    """Node class."""

    def __init__(self, value=None, left=None, right=None):
        """Init of the Node class."""
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """Binary Search Tree."""

    """insert(self, val): will insert the value val into the BST. If val is already present, it will be ignored."""
    """search(self, val): will return the node containing that value, else None"""
    """size(self): will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty."""
    """depth(self): will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc."""
    """contains(self, val): will return True if val is in the BST, False if not."""
    """balance(self): will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0."""
    """in_order(self): will return a generator that will return the values in the tree using in-order traversal, one at a time."""
    """pre_order(self): will return a generator that will return the values in the tree using pre-order traversal, one at a time."""
    """post_order(self): will return a generator that will return the values in the tree using post_order traversal, one at a time."""
    """breadth_first(self): will return a generator that will return the values in the tree using breadth-first traversal, one at a time."""

    def __init__(self, if_iter=None):
        """Init of the Binary Search Tree class."""
        self.root = None
        self.counter = 0
        self.container = []
        if if_iter:
            try:
                for value in if_iter:
                    self.insert(value)
            except TypeError:
                self.insert(if_iter)
        self._in_order = self.in_order_trav()
        self._pre_order = self.pre_order_trav()
        self._post_order = self.post_order_trav()

    def insert(self, val):
        """Take a value, inserts into Binary Search Tree at correct placement."""
        if self.root is None:
            self.root = Node(val)
            self.counter += 1
            self.container.append(val)

        else:
            vertex = self.root
            while True:
                if val > vertex.value:
                    if vertex.right:
                        vertex = vertex.right
                    else:
                        vertex.right = Node(val)
                        self.counter += 1
                        self.container.append(val)
                        break

                elif val < vertex.value:
                    if vertex.left:
                        vertex = vertex.left
                    else:
                        vertex.left = Node(val)
                        self.counter += 1
                        self.container.append(val)
                        break
                else:
                    break

    def size(self):
        """Return size of Binary Search Tree."""
        return self.counter

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        return val in self.container

    def search(self, val):
        """Return the node containing that value, else None."""
        vertex = self.root
        while vertex:
            if val > vertex.value:
                if not vertex.right:
                    return None
                vertex = vertex.right
            elif val < vertex.value:
                if not vertex.left:
                    return None
                vertex = vertex.left
            else:
                return vertex
        return None

    def depth(self):
        """
        Return an integer representing the total number of levels in the tree.

        If there is one value, the depth should be 1, if two values it will be 2,
        if three values it may be 2 or three, depending, etc.
        """
        return self.calc_depth(self.root)

    def calc_depth(self, tree):
        """Calculate the depth of the binary search tree recursively."""
        if tree is None:
            return 0
        else:
            return max(self.calc_depth(tree.right), self.calc_depth(tree.left)) + 1

    def balance(self):
        """
        Return an integer, positive or negative that represents how well balanced the tree is.

        Trees which are higher on the left than the right should return a positive value,
        trees which are higher on the right than the left should return a negative value.
        An ideally-balanced tree should return 0.
        """
        if self.root is None:
            return 0
        return self.calc_depth(self.root.right) - self.calc_depth(self.root.left)

    def in_order(self):
        """Return."""
        return next(self._in_order)

    def in_order_trav(self):
        """Traverse in_order, yielding via generator."""
        vertex = self.root
        visited = []
        while (visited or vertex is not None):

            if vertex is not None:
                visited.append(vertex)
                vertex = vertex.left
            else:
                vertex = visited.pop()
                yield vertex.value
                vertex = vertex.right

    def pre_order(self):
        """Return."""
        return next(self._pre_order)

    def pre_order_trav(self):
        """Traverse pre_order, yielding via generator."""
        vertex = self.root
        visited = []
        while (visited or vertex is not None):
            if vertex is not None:
                yield vertex.value
                visited.append(vertex)
                vertex = vertex.left
            else:
                vertex = visited.pop()
                vertex = vertex.right

    def post_order(self):
        """Return."""
        return next(self._post_order)

    def post_order_trav(self):
        """Traverse pre_order, yielding via generator."""
        vertex = self.root
        peek_vertex = None
        last_vertex = None
        visited = []
        while (visited or vertex is not None):
            if vertex is not None:
                visited.append(vertex)
                vertex = vertex.left
            else:
                peek_vertex = visited[-1]
                if peek_vertex.right and peek_vertex.right is not last_vertex:
                    vertex = peek_vertex.right
                else:
                    yield peek_vertex.value
                    last_vertex = visited.pop()

    def breadth_first(self):
        """Fill in later."""
        return next(self._breadth_first)

    def breadth_first_trav(self):
        """Traverse breadth first order, yielding a generator."""
        q = Queue()
        q.enqueue(self.root)
        while len(q) > 0:
            vertex = q.dequeue()
            yield vertex.value
            if (vertex.left):
                q.enqueue(vertex.left)
            if (vertex.right):
                q.enqueue(vertex.right)
