"""This module implements a binary search tree."""

from queue_ds import Queue
from stack import Stack


class Node(object):
    """Node object for use in a binary search tree."""

    def __init__(self, value, right=None, left=None, parent=None):
        """Initialize a node for a binary search tree object."""
        self.value = value
        self.right = right
        self.left = left
        self.parent = parent

    def _has_children(self):
        """Return True or False if Node has children."""
        if self.right or self.left:
            return True
        return False

    def _return_children(self):
        """Return all children of a Node."""
        if self.left and self.right:
            return [self.left, self.right]
        elif self.left or self.right:
            return [self.left] if self.left else [self.right]


class BinarySearchTree(object):
    """Binary Search Tree Object.

    Methods:
      - insert(self, val): will insert the value val into the BST. If
        val is already present, it will be ignored.
      - search(self, val): will return the node containing that value,
        else None
      - size(self): will return the integer size of the BST (equal to
        the total number of values stored in the tree). It will return 0
        if the tree is empty.
      - depth(self): will return an integer representing the total number
        of levels in the tree. If there is one value, the depth should be
        1, if two values it will be 2, if three values it may be 2 or three,
        depending, etc.
      - contains(self, val): will return True if val is in the BST, False
        if not.
      - balance(self): will return an integer, positive or negative that
        represents how well balanced the tree is. Trees which are higher
        on the left than the right should return a positive value, trees
        which are higher on the right than the left should return a negative
        value. An ideally-balanced tree should return 0.
      - in_order(self): will return a generator that will return the values
        in the tree using in-order traversal, one at a time.
      - pre_order(self): will return a generator that will return the values
        in the tree using pre-order traversal, one at a time.
      - post_order(self): will return a generator that will return the values
        in the tree using post_order traversal, one at a time.
      - breadth_first(self): will return a generator that will return the
        values in the tree using breadth-first traversal, one at a time.
    """

    def __init__(self):
        """Initialize a Binary Search Tree object."""
        self.root = None
        self._size = 0

    def insert(self, val):
        """Insert a new node with val into the BST."""
        curr_node = self.root
        new_node = Node(val)
        if curr_node is None:
            self.root = new_node
            self._size = 1
            return

        while curr_node:
            if val > curr_node.value:
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = new_node
                    new_node.parent = curr_node
                    self._size += 1
                    break
            elif val < curr_node.value:
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = new_node
                    new_node.parent = curr_node
                    self._size += 1
                    break
            else:
                return
        self._test_tree_balance(new_node)

    def search(self, val):
        """Return the node with value val or return None."""
        start = self.root
        if start is None:
            raise ValueError("Cannot search an empty tree.")
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
        return self._size

    def __len__(self):
        """Return integer size of the BST."""
        return self.size()

    def depth(self, start=''):
        """Return the integer depth of the BST."""
        def depth_wrapped(start):
            if start is None:
                return 0
            else:
                right_depth = depth_wrapped(start.right)
                left_depth = depth_wrapped(start.left)
                return max(right_depth, left_depth) + 1
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

    def find_balance(self, start=None):
        """Return positive or negative integer that represents tree balance."""
        if start is None:
            start = self.root
        if start is None:
            return 0
        return self.depth(start.left) - self.depth(start.right)

    def in_order(self, node=None):
        """Return a generator of the tree in in_order order."""
        start = node
        if start is None:
            start = self.root
        if start is None:
            raise StopIteration
        s = Stack()
        while len(s) or start:
            if start:
                s.push(start)
                start = start.left
            else:
                start = s.pop()
                yield start.value
                start = start.right

    def pre_order(self):
        """Return a generator of the tree in pre_order order."""
        start = self.root
        if start is None:
            raise StopIteration
        s = Stack()
        s.push(start)
        while len(s):
            curr = s.pop()
            yield curr.value
            if curr.right is not None:
                s.push(curr.right)
            if curr.left is not None:
                s.push(curr.left)

    def post_order(self):
        """Return a generator of the tree in post_order order."""
        start = self.root
        if start is None:
            raise StopIteration
        s = []
        last = None
        while s or start:
            if start:
                s.append(start)
                start = start.left
            else:
                peek = s[-1]
                if peek.right and last is not peek.right:
                    start = peek.right
                else:
                    yield peek.value
                    last = s.pop()

    def breadth_first(self):
        """Return a generator of the tree in breadth first traversal order."""
        start = self.root
        if start is None:
            raise StopIteration
        q = Queue()
        q.enqueue(start)

        while len(q) > 0:
            current = q.dequeue()
            yield current.value

            if current._has_children():
                for child in current._return_children():
                    q.enqueue(child)

    def delete(self, val):
        """Delete a node."""
        if self.size() == 0:
            raise IndexError("Cannot delete from empty tree.")
        target = self.search(val)
        if target is None:
            raise ValueError("Cannot delete node that does not exist.")
        test_node = target.parent
        if self.size() == 1:
            self.root = None
            self._size -= 1
            return
        if not target._has_children():
            self._del_leaf(target)
        elif len(target._return_children()) == 1:
            self._swap_par_child(target)
        else:
            g = self.in_order()
            gen_out = None
            while gen_out is not val:
                gen_out = next(g)
            successor = self.search(next(g))
            target.value = successor.value
            test_node = successor
            if not successor._has_children():
                self._del_leaf(successor)
            else:
                self._swap_par_child(successor)

        self._size -= 1
        self._test_tree_balance(test_node)

    def _del_leaf(self, node):
        """Given a leaf node, delete it from tree."""
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None
        node.parent = None

    def _swap_par_child(self, node):
        """Given a node with one child swap, parent child and del node."""
        if node is node.parent.left:
            node.parent.left = node._return_children()[0]
        else:
            node.parent.right = node._return_children()[0]
        node.parent = None

    def _rotate_right(self, sub_root):
        """Given root and pivot nodes, complete a right rotation."""
        pivot = sub_root.left
        sub_root.left = pivot.right
        if pivot.right is not None:
            pivot.right.parent = sub_root
        pivot.parent = sub_root.parent
        if sub_root is self.root:
            self.root = pivot
        else:
            if sub_root is sub_root.parent.right:
                    sub_root.parent.right = pivot
            else:
                sub_root.parent.left = pivot
        pivot.right = sub_root
        sub_root.parent = pivot

    def _rotate_left(self, sub_root):
        """Give root and pivot nodes, complete a left rotation."""
        pivot = sub_root.right
        sub_root.right = pivot.left
        if pivot.left is not None:
            pivot.left.parent = sub_root
        pivot.parent = sub_root.parent
        if sub_root is self.root:
            self.root = pivot
        else:
            if sub_root is sub_root.parent.left:
                    sub_root.parent.left = pivot
            else:
                sub_root.parent.right = pivot
        pivot.left = sub_root
        sub_root.parent = pivot

    def _test_tree_balance(self, node):
        """Check balance of tree."""
        while node:
            bal = self.find_balance(node)
            if abs(bal) >= 2:
                self._balance_tree(node, bal)
            node = node.parent

    def _balance_tree(self, start_node, bal):
        """Balance subtree of start node."""
        if bal > 0:                             #< --- Heavy on the left.
            sub_bal = self.find_balance(start_node.left)
            if sub_bal < 0:                     #< --- Sub, right heavy
                self._rotate_left(start_node.left)
            self._rotate_right(start_node)
        else:                                   #< --- Heavy on the right.
            sub_bal = self.find_balance(start_node.right)
            if sub_bal > 0:                     #< --- Sub, left heavy
                self._rotate_right(start_node.right)
            self._rotate_left(start_node)
        return self.depth(self.root.left) - self.depth(self.root.right)
