"""
    insert(self, string): will insert the input string into the trie. If character in the input string is already present, it will be ignored.
    contains(self, string): will return True if the string is in the trie, False if not.
    size(self): will return the total number of words contained within the trie. 0 if empty.
    remove(self, string): will remove the given string from the trie. If the word doesn’t exist, will raise an appropriate exception.
"""


class Node(object):

    def __init__(self, val=None):
        self.val = val
        self.nodes = {}


class Trie(object):

    def __init__(self):
        self.root = Node('*')
        self.size = 0

    def insert(self, word):
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
            self.size += 1
            node.nodes['$'] = None

    def contains(self, word):
        node = self.root
        for each in word:
            if each in node.nodes:
                node = node.nodes[each]
            else:
                return False
        if '$' in node.nodes:
            return True
        return False

    def size(self, size):
        return self.size

    def remove(self, word):
        node_list = []
        node = self.root
        for each in word:
            if each in node.nodes:
                node_list.append(node)
                node = node.nodes[each]
                continue
        last = node_list.pop()
        if '$' not in last.nodes:
            return
        del last.nodes['$']
        for i in range(len(node_list)):
            last_val = last.val
            last = node_list.pop()
            if len(last.nodes) > 1:
                return
            del last.nodes[last_val]


# class Node(object):
#     """Node class."""

#     def __init__(self, value=None, left=None, right=None):
#         """Init of the Node class."""
#         self.value = value
#         self.node = node
#         self.right = right
#         self.parent = None
