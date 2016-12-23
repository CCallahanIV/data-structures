"""This module implements a graph data structure."""


class Graph(object):
    """Define a class datastructure.

    g.nodes(): return a list of all nodes in the graph
    g.edges(): return a list of all edges in the graph
    g.add_node(n): adds a new node ‘n’ to the graph
    g.add_edge(n1, n2): adds a new edge to the graph connecting ‘n1’ and ‘n2’, if either n1 or n2 are not already present in the graph, they should be added.
    g.del_node(n): deletes the node ‘n’ from the graph, raises an error if no such node exists
    g.del_edge(n1, n2): deletes the edge connecting ‘n1’ and ‘n2’ from the graph, raises an error if no such edge exists
    g.has_node(n): True if node ‘n’ is contained in the graph, False if not.
    g.neighbors(n): returns the list of all nodes connected to ‘n’ by edges, raises an error if n is not in g
    g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g

    """

    def __init__(self):
        """Initialize a graph data structure."""
        self._gdict = {}

    def nodes(self):
        """Return a list of all nodes in the graph."""
        pass

    def edges(self):
        """Return a list of all edges in the graph."""
        pass

    def add_node(self, n):
        """Add a new node to the graph."""
        pass

    def add_edge(self, n1, n2):
        """Add a new edge to the graph connecting n1 and n2."""
        pass

    def del_node(self, n):
        """Delete node n from the graph."""
        pass

    def del_edge(self, n1, n2):
        """Delete the edge connecting node 1 and node 2."""
        pass

    def has_node(self, n):
        """Return True if node n exists in the graph."""
        pass

    def neighbors(self, n):
        """Return a list of all neighbors of node n."""
        pass

    def adjacent(self, n1, n2):
        """Return true if there is an edge connecting n1 and n2."""
        pass
