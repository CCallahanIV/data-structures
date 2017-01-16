"""This module implements a graph data structure."""

from queue_ds import Queue
import timeit
import random


class Graph(object):
    """Define a graph datastructure.

    Methods:

        g.nodes(): return a list of all nodes in the graph
        g.edges(): return a list of all edges in the graph
        g.add_node(n): adds a new node 'n' to the graph
        g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not already present in the graph, they should be added.
        g.del_node(n): deletes the node 'n' from the graph, raises an error if no such node exists
        g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no such edge exists
        g.has_node(n): True if node 'n' is contained in the graph, False if not.
        g.neighbors(n): returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g
        g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g

    """

    def __init__(self):
        """Initialize a graph data structure."""
        self._gdict = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        return list(self._gdict.keys())

    def edges(self):
        """Return a list of all edges in the graph."""
        edge_list = []
        for key in self._gdict:
            for neighbor in self._gdict[key]:
                edge_list.append((key, neighbor))
        return edge_list

    def add_node(self, n):
        """Add a new node to the graph."""
        self._gdict.setdefault(n, [])

    def add_edge(self, n1, n2):
        """Add a new edge to the graph connecting n1 and n2."""
        if n1 == n2:
            raise KeyError("Edges cannot connect a node to itself.")
        if n1 in self._gdict and n2 in self._gdict[n1]:
            return
        self._gdict.setdefault(n1, []).append(n2)
        self.add_node(n2)

    def del_node(self, n):
        """Delete node n from the graph."""
        try:
            del self._gdict[n]
            for key in self._gdict:
                if n in self._gdict[key]:
                    self._gdict[key].remove(n)
        except KeyError:
            raise KeyError("Can't delete a node if it doesn't already exist.")

    def del_edge(self, n1, n2):
        """Delete the edge connecting node 1 and node 2."""
        try:
            self._gdict[n1].remove(n2)
        except ValueError:
            raise ValueError("That edge does not exist.")
        except KeyError:
            raise KeyError("The node n1 does not exist.")

    def has_node(self, n):
        """Return True if node n exists in the graph."""
        return n in self._gdict

    def neighbors(self, n):
        """Return a list of all neighbors of node n."""
        try:
            return self._gdict[n]
        except KeyError:
            raise KeyError("Node {} does not exist".format(n))

    def adjacent(self, n1, n2):
        """Return true if there is an edge connecting n1 and n2."""
        if n1 in self._gdict:
            if n2 in self._gdict:
                return n2 in self._gdict[n1]
            else:
                raise KeyError("The node {} is not in the graph.".format(n2))
        else:
            raise KeyError("The node {} is not in the graph.".format(n1))

    def depth_first_traversal(self, start, path=None):
        """Traverse a graph depth first."""
        if start not in self._gdict:
            raise KeyError(start, "not in graph.")
        if path is None:
            path = []
        path.append(start)
        for neighbor in self._gdict[start]:
            if neighbor not in path:
                self.depth_first_traversal(neighbor, path)

        return path

    def breadth_first_traversal(self, start):
        """Traverse a graph breadth first."""
        if start not in self._gdict:
            raise KeyError(start, "not in graph.")
        path = []
        q = Queue()
        q.enqueue(start)

        while len(q) > 0:
            current = q.dequeue()
            if current not in path:
                path.append(current)

            for neighbor in self._gdict[current]:
                if neighbor not in path:
                    q.enqueue(neighbor)

        return path


def make_graph():
        nodes = range(0, 100)
        g = Graph()
        for node in nodes:
            for i in range(random.randint(1, 50)):
                b = random.choice(nodes)
                if node == b:
                    continue
                g.add_edge(node, b)
        return g


def depth(g):
        return g.depth_first_traversal(0)


def breadth(g):
        return g.breadth_first_traversal(0)

g = make_graph()

if __name__ == "__main__":

    res1 = timeit.repeat(stmt="depth(g)", setup="from graph import g, depth", number=10, repeat=3)
    res2 = timeit.repeat(stmt="breadth(g)", setup="from graph import g, breadth", number=10, repeat=3)
    print("Depth First: ", res1)
    print("Breadth First: ", res2)
