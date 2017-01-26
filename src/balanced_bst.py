"""Module for Binary Search Tree."""

from queue_ds import Queue
import timeit
import random


class Node(object):
    """Node class."""

    def __init__(self, value=None, left=None, right=None):
        """Init of the Node class."""
        self.value = value
        self.left = left
        self.right = right
        self.parent = None


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
        if if_iter:
            try:
                for value in if_iter:
                    self.insert(value)
            except TypeError:
                self.insert(if_iter)
        self._in_order = self._in_order_trav()
        self._pre_order = self._pre_order_trav()
        self._post_order = self._post_order_trav()
        self._breadth_first = self._breadth_first_trav()

    def size(self):
        """Return size of Binary Search Tree."""
        return self.counter

    def contains(self, val):
        """Return True if val is in the BST, False if not."""
        if self.search(val):
            return True
        return False

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
        return self._calc_depth(self.root)

    def _calc_depth(self, tree):
        """Calculate the depth of the binary search tree recursively."""
        if tree is None:
            return 0
        else:
            return max(self._calc_depth(tree.right), self._calc_depth(tree.left)) + 1

    def balance(self):
        """
        Return an integer, positive or negative that represents how well balanced the tree is.

        Trees which are higher on the left than the right should return a positive value,
        trees which are higher on the right than the left should return a negative value.
        An ideally-balanced tree should return 0.
        """
        if self.root is None:
            return 0
        return self._calc_balance(self.root)

    def _calc_balance(self, node):
        """Calculate the balance of a subtree at node."""
        return self._calc_depth(node.right) - self._calc_depth(node.left)

    def in_order(self):
        """Return the next value from the generator _in_order."""
        return next(self._in_order)

    def _in_order_trav(self):
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
        """Return the next value from the generator _pre_order."""
        return next(self._pre_order)

    def _pre_order_trav(self):
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
        """Return the next value from the generator _post_order."""
        return next(self._post_order)

    def _post_order_trav(self):
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
        """Return the next value from the generator _breadth_first."""
        return next(self._breadth_first)

    def _breadth_first_trav(self):
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

    def insert(self, val):
        """Take a value, inserts into Binary Search Tree at correct placement."""
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
                        new_node = Node(val)
                        vertex.right = new_node
                        new_node.parent = vertex
                        self.counter += 1
                        break

                elif val < vertex.value:
                    if vertex.left:
                        vertex = vertex.left
                    else:
                        new_node = Node(val)
                        vertex.left = new_node
                        new_node.parent = vertex
                        self.counter += 1
                        break
                else:
                    break
        self._balance_tree()

    def delete(self, val):
        """Remove val from the tree if present, if not present this method is a no-op. Return None in all cases."""
        vertex = self.root
        parent_of_del = None
        del_node = None
        if self.root is None:
            return
        if self.root.value == val:
            left = self.root.left
            right = self.root.right
            if not right:
                self.root = self.root.left
                self.root.parent = None
                self.counter -= 1
                self._balance_tree()
                return
            if not right.left:
                self.root = right
                self.root.left = left
                self.root.parent = None
                self.counter -= 1
                self._balance_tree()
                return
            vertex = vertex.right
            while True:
                if not vertex.left.left:
                    min_parent = vertex
                    break
                else:
                    vertex = vertex.left
            min_node = min_parent.left
            min_parent.left = min_node.right
            if min_parent.left:
                min_parent.left.parent = min_parent
            self.root = min_node
            self.root.left = left
            self.root.right = right
            self.root.parent = None
            self.counter -= 1
            self._balance_tree()
        else:
            while True:
                if vertex.right and val == vertex.right.value:
                    parent_of_del = vertex
                    del_node = parent_of_del.right
                    min_parent = self._find_min_parent(parent_of_del, "right")
                    break
                elif vertex.left and val == vertex.left.value:
                    parent_of_del = vertex
                    del_node = parent_of_del.left
                    min_parent = self._find_min_parent(parent_of_del, "left")
                    break
                elif val > vertex.value and vertex.right:
                    vertex = vertex.right
                elif val < vertex.value and vertex.left:
                    vertex = vertex.left
                else:
                    self._balance_tree()
                    return

            if parent_of_del.right and val == parent_of_del.right.value:
                if not min_parent:
                    parent_of_del.right = None
                    self.counter -= 1
                    self._balance_tree()
                    return
                if min_parent is del_node:
                    right = del_node.right
                    del_node_left = del_node.left
                    parent_of_del.right = right
                    if right:
                        right.parent = parent_of_del
                    parent_of_del.right.left = del_node_left
                    if del_node_left:
                        del_node_left.parent = parent_of_del.right
                    self.counter -= 1
                    self._balance_tree()
                    return
                left = del_node.left
                right = del_node.right
                min_node = min_parent.left
                min_parent.left = min_node.right
                if min_parent.left:
                    min_parent.left.parent = min_parent
                del_node = min_node
                del_node.right = right
                if right:
                    del_node.right.parent = del_node
                del_node.left = left
                if left:
                    del_node.left.parent = del_node
                parent_of_del.right = del_node
                if del_node:
                    parent_of_del.right.parent = parent_of_del
                self.counter -= 1
                self._balance_tree()

            elif parent_of_del.left and val == parent_of_del.left.value:
                if not min_parent:
                    parent_of_del.left = None
                    self.counter -= 1
                    self._balance_tree()
                    return
                if min_parent is del_node:
                    left = del_node.right
                    del_node_left = del_node.left
                    parent_of_del.left = left
                    if left:
                        left.parent = parent_of_del
                    parent_of_del.left.left = del_node_left
                    if del_node_left:
                        del_node_left.parent = parent_of_del.right
                    self.counter -= 1
                    self._balance_tree()
                    return
                left = del_node.left
                right = del_node.right
                min_node = min_parent.left
                min_parent.left = min_node.right
                if min_parent.left:
                    min_parent.left.parent = min_parent
                del_node = min_node
                del_node.right = right
                if right:
                    del_node.right.parent = del_node
                del_node.left = left
                if left:
                    del_node.left.parent = del_node
                parent_of_del.left = del_node
                if del_node:
                    parent_of_del.left.parent = parent_of_del
                self.counter -= 1
                self._balance_tree()

    def _find_min_parent(self, vertex, side):
        """Find the parent of the replacement node, given the parent of the delete node."""
        if side == "right":
            if not vertex.right.right and not vertex.right.left:
                return
            if vertex.right.right and not vertex.right.right.left:
                return vertex.right
            elif vertex.right.right and vertex.right.right.left:
                vertex = vertex.right.right
                while True:
                    if not vertex.left.left:
                        return vertex
                    else:
                        vertex = vertex.left
        else:
            if not vertex.left.right and not vertex.left.left:
                return
            if vertex.left.right and not vertex.left.right.left:
                return vertex.left
            elif vertex.left.right and vertex.left.right.left:
                vertex = vertex.left.right
                while True:
                    if not vertex.left.left:
                        return vertex
                    else:
                        vertex = vertex.left
        return

    def _balance_tree(self):
        for node in self._post_order_node():
            if self._calc_balance(node) > 1:
                if self._calc_balance(node.right) < 0:
                    self._right_left_rotation(node)
                else:
                    self._left_rotation(node)
            elif self._calc_balance(node) < -1:
                if self._calc_balance(node.left) > 0:
                    self._left_right_rotation(node)
                else:
                    self._right_rotation(node)

    def _left_rotation(self, node):
        a = node
        a_parent = a.parent
        b = a.right
        d = b.left
        if a is self.root:
            self.root = b
            self.root.parent = None
            self.root.left = a
            a.parent = self.root
            a.right = d
            if d:
                d.parent = a
            return
        a_parent.right = b
        b.parent = a_parent
        b.left = a
        a.parent = b
        a.right = d
        if d:
            d.parent = a

    def _right_rotation(self, node):
        a = node
        a_parent = a.parent
        b = a.left
        d = b.right
        if a is self.root:
            self.root = b
            self.root.parent = None
            self.root.right = a
            a.parent = self.root
            a.left = d
            if d:
                d.parent = a
            return
        a_parent.left = b
        b.parent = a_parent
        b.right = a
        a.parent = b
        a.left = d
        if d:
            d.parent = a

    def _left_right_rotation(self, node):
        """Try left right rotation on node."""
        # if self._calc_balance(node.left) > 0:
        if node.left.right.left:
            vertex = node
            left_head = node.left
            right_sub = node.left.right
            switcher = node.left.right.left
            # if node.left.right.left:
            #     switcher = node.left.right.left
            if vertex.parent:
                right_sub.parent = vertex.parent
                if vertex.parent.value > vertex.value:
                    vertex.parent.left = right_sub
                else:
                    vertex.parent.right = right_sub
            else:
                self.root = right_sub
                right_sub.parent = None
            switcher.parent = left_head
            # if node.left.right.left:
            #     switcher.parent = left_head
            left_head.parent = right_sub
            left_head.right = switcher
            # if node.left.right.left:
            #     left_head.right = switcher
            right_sub.right = vertex
            right_sub.left = left_head
            vertex.parent = right_sub
            vertex.left = None
        else:
            vertex = node
            left_head = node.left
            right_sub = node.left.right
            switcher = node.left.right.right
            # if node.left.right.right:
            #     switcher = node.left.right.right
            if vertex.parent:
                right_sub.parent = vertex.parent
                if vertex.parent.value > vertex.value:
                    vertex.parent.left = right_sub
                else:
                    vertex.parent.right = right_sub
            else:
                self.root = right_sub
                right_sub.parent = None
            switcher.parent = vertex
            vertex.left = switcher
            # if node.left.right.right:
            #     switcher.parent = vertex
            # if node.left.right.right:
            #     vertex.left = switcher
            vertex.parent = right_sub
            right_sub.right = vertex
            right_sub.left = left_head
            left_head.parent = right_sub
            left_head.right = None

    def _right_left_rotation(self, node):
        """Try right left rotation on node."""
        if node.right.left.left:
        # if self._calc_balance(node.right) < 0:
            vertex = node
            right_head = node.right
            left_sub = node.right.left
            switcher = node.right.left.left
            # if node.right.left.left:
            #     switcher = node.right.left.left
            if vertex.parent:
                left_sub.parent = vertex.parent
                if vertex.parent.value > vertex.value:
                    vertex.parent.left = left_sub
                else:
                    vertex.parent.right = left_sub
            else:
                self.root = left_sub
                left_sub.parent = None
            switcher.parent = right_head
            # if node.right.left.left:
            #     switcher.parent = right_head
            right_head.parent = vertex
            right_head.left = None
            left_sub.right = right_head
            left_sub.left = vertex
            vertex.parent = left_sub
            vertex.right = switcher
            # if node.right.left.left:
            #     vertex.right = switcher
            # else:
            #     vertex.right = None
        else:
            # import pdb; pdb.set_trace()
            vertex = node
            right_head = node.right
            left_sub = node.right.left
            switcher = node.right.left.right
            # if node.right.left.right:
            #     switcher = node.right.left.right
            if vertex.parent:
                left_sub.parent = vertex.parent
                if vertex.parent.value > vertex.value:
                    vertex.parent.left = left_sub
                else:
                    vertex.parent.right = left_sub
            else:
                self.root = left_sub
                left_sub.parent = None
            switcher.parent = right_head
            # if node.right.left.right:
            #     switcher.parent = right_head
            vertex.right = None
            vertex.parent = left_sub
            left_sub.left = vertex
            left_sub.right = right_head
            right_head.left = switcher
            # if node.right.left.right:
            #     right_head.left = switcher
            right_head.parent = left_sub

    def _post_order_node(self):
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
                    yield peek_vertex
                    last_vertex = visited.pop()

    # def balance(self):
    #     """
    #     Return an integer, positive or negative that represents how well balanced the tree is.

    #     Trees which are higher on the left than the right should return a positive value,
    #     trees which are higher on the right than the left should return a negative value.
    #     An ideally-balanced tree should return 0.
    #     """
    #     if self.root is None:
    #         return 0
    #     return self._calc_depth(self.root.right) - self._calc_depth(self.root.left)


    # def print_bst(self):
    #     """Return."""
    #     thislevel = [self.root]
    #     while thislevel:
    #         nextlevel = []
    #         print_level = []
    #         counter = 0
    #         for n in thislevel:
    #             print(print_level[counter])
    #             if n.left:
    #                 nextlevel.append(n.left)
    #                 print_level.append(n.left.value)
    #             else:
    #                 print_level.append('_')
    #             if n.right:
    #                 nextlevel.append(n.right)
    #                 print_level.append(n.right.value)
    #             else:
    #                 print_level.append('_')
    #         print()
    #         thislevel = nextlevel



# if __name__ == "__main__":

#     res1 = timeit.repeat(stmt="depth(g)", setup="from graph import g, depth", number=10, repeat=3)
#     res2 = timeit.repeat(stmt="breadth(g)", setup="from graph import g, breadth", number=10, repeat=3)
#     print("Depth First: ", res1)
#     print("Breadth First: ", res2)
