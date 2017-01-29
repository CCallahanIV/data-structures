"""Module for Trie tree with traversal."""

# TRIE TREE TRAVERSAL (TTT)
#
# CodeFellows 401d5
# Submission Date:
#
# Authors:  Colin Lamont <https://github.com/chamberi>
#           Ben Shields <https://github.com/iamrobinhood12345>
#
# URL:

from collections import OrderedDict


class Node(object):
    """Node Class contains a value and a dictionary of nodes."""

    def __init__(self, val=None):
        """Initialize the Node class with val and empty nodes dictionary."""
        self.val = val
        self.nodes = OrderedDict()


class Trie(object):
    """Trie class, which is the Trie tree."""

    """
        insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.
        contains(self, string): will return True if the string is in the trie, False if not.
        size(self): will return the total number of words contained within the trie. 0 if empty.
        remove(self, string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception.
    """

    def __init__(self):
        """Initialize the Trie class with root Node with ('*') and size of 0."""
        self.root = Node('*')
        self._size = 0

    def insert(self, word):
        """Insert method, which takes a word and inserts each letter of the word into the Trie, with pointer to next Node or $ if end.""" 
        node = self.root
        new_node = None
        new_word = False
        for each in word:
            if each in node.nodes:
                node = node.nodes[each]
                continue
            new_word = True
            new_node = Node(each)
            node.nodes[each] = new_node
            node = new_node
        if new_word:
            self._size += 1
            node.nodes['$'] = None

    def contains(self, word):
        """The contains method returns True if the word is found in the Trie tree, or False if not."""
        node = self.root
        for each in word:
            if each in node.nodes:
                node = node.nodes[each]
            else:
                return False
        if '$' in node.nodes:
            return True
        return False

    def size(self):
        """The size method returns the number of words in the Trie."""
        return self._size

    def remove(self, word):
        """The remove method removes the word from the Trie."""
        node_list = []
        node = self.root
        for each in word:
            if each in node.nodes:
                node_list.append(node.nodes[each])
                node = node.nodes[each]
        last = node_list.pop()
        if '$' not in last.nodes:
            return
        del last.nodes['$']
        for i in range(len(node_list)):
            last_val = last.val
            last = node_list.pop()
            if '$' in last.nodes:
                self._size -= 1
                break
            if len(last.nodes) > 1:
                del last.nodes[last_val]
                self._size -= 1
                break
            del last.nodes[last_val]

    def traversal(self, start=None):
        """A generator yielding values in the tree in depth first order."""
        if not start:
            stack = []
            stack.append(self.root)
            while len(stack) > 0:
                node = stack.pop()
                if node.val != '*':
                    yield node.val
                items = node.nodes.items()
                items = reversed(items)
                nodes = OrderedDict(items)
                for each in nodes:
                    if len(node.nodes) == 1 and '$' in node.nodes:
                        break
                    stack.append(nodes[each])
        else:
            word = ''
            stack = []
            branch_node = None
            to_yield = False
            stack.append(self.root)
            while len(stack) > 0:
                node = stack.pop()
                word += node.val
                if to_yield:
                    yield node.val
                if start in word:
                    to_yield = True
                    branch_node = node
                items = node.nodes.items()
                items = reversed(items)
                nodes = OrderedDict(items)
                for each in nodes:
                    if len(node.nodes) == 1 and '$' in node.nodes:
                        break
                    stack.append(nodes[each])

        stack = []
        stack.append(self.root)
        while len(stack) > 0:
            node = stack.pop()
            if node.val != '*':
                yield node.val
            items = node.nodes.items()
            items = reversed(items)
            nodes = OrderedDict(items)
            for each in nodes:
                if len(node.nodes) == 1 and '$' in node.nodes:
                    break
                stack.append(nodes[each])

    def _traversal(self, node):

        stack = []
        stack.append(node)
        while len(stack) > 0:
            node = stack.pop()
            if node.val != '*':
                yield node.val
            items = node.nodes.items()
            items = reversed(items)
            nodes = OrderedDict(items)
            for each in nodes:
                if len(node.nodes) == 1 and '$' in node.nodes:
                    break
                stack.append(nodes[each])


    # def traversal(self, start=None):
    #     """The traversal method does a depth first traversal of the trie to find instances of start and return the rest."""
    #     g = self._traversal(self.root)
    #     yield next(g)

    # def _find_start(self, start):
    #     """Return the next instance of start string."""
    #     pass

    # def _traversal(self, node):
    #     """Recursive helper method for traversal. Yields value at node."""
    #     print('111111111111111111111')
    #     import pdb; pdb.set_trace()
    #     if len(node.nodes) == 1 and '$' in node.nodes:
    #         print('2222222222222222222')
    #         yield node.val
    #         return
    #     yield node.val
    #     for each in node.nodes:
    #         print('333333333333333333')
    #         print('each', each)
    #         print('node.nodes[each]', node.nodes[each])
    #         print(node.nodes)
    #         h = self._traversal(node.nodes[each])
    #         yield next(h)
