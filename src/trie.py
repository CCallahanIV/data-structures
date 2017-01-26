class Node(object):

    def __init__(self, val):
        self.val = None
        self.nodes = {}


class Trie(object):

    def __init(self):
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
            new_node = Node('each')
            node.nodes[each] = new_node
            node = new_node
        if new_word:
            self.size += 1
            node['$'] = None

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
