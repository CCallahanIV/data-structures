"""This module contains an implementation of a weighted graph."""

from queue_ds import Queue


class WGraph(object):
    """Define a class datastructure.

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
        """Initialize a weighted graph data structure."""
        self._gdict = {}

    def nodes(self):
        """Return a list of all nodes in the weighted graph."""
        return list(self._gdict)

    def edges(self):
        """Return a list of all edges in the weighted graph."""
        edge_list = []
        for key in self._gdict:
            for neighbor in list(self._gdict[key]):
                edge_list.append((key, neighbor, self._gdict[key][neighbor]))
        return edge_list

    def add_node(self, n):
        """Add a new node to the weighted graph."""
        self._gdict.setdefault(n, {})

    def add_edge(self, n1, n2, weight):
        """Add a new edge to the weighted graph connecting n1 and n2."""
        if n1 == n2:
            raise KeyError("Edges cannot connect a node to itself.")
        if n1 in self._gdict and n2 in self._gdict[n1]:
            return
        self._gdict.setdefault(n1, {})[n2] = weight
        self.add_node(n2)

    def del_node(self, n):
        """Delete node n from the weighted graph."""
        try:
            del self._gdict[n]
            for key in self._gdict:
                if n in self._gdict[key]:
                    del self._gdict[key][n]
        except KeyError:
            raise KeyError("Can't delete a node if it doesn't already exist.")

    def del_edge(self, n1, n2):
        """Delete the edge connecting node 1 and node 2."""
        try:
            del self._gdict[n1][n2]
        except KeyError:
            raise KeyError("That edge does not exist.")

    def has_node(self, n):
        """Return True if node n exists in the weighted graph."""
        if n in self._gdict:
            return True
        return False

    def neighbors(self, n):
        """Return a dictionary of all neighbors and their weights of node n."""
        try:
            return self._gdict[n]
        except KeyError:
            raise KeyError("Node {} does not exist".format(n))

    def adjacent(self, n1, n2):
        """Return true if there is an edge connecting n1 and n2."""
        if n1 in self._gdict:
            if n2 in self._gdict:
                if n2 in self._gdict[n1]:
                    return True
                return False
            else:
                raise KeyError("The node {} is not in the graph.".format(n2))
        else:
            raise KeyError("The node {} is not in the graph.".format(n1))

    def depth_first_traversal(self, start, path=None):
        """Traverse a weighted graph depth first."""
        if start not in self._gdict:
            raise KeyError(start, "not in graph.")
        if path is None:
            path = []
        path.append(start)
        for neighbor in list(self._gdict[start]):
            if neighbor not in path:
                self.depth_first_traversal(neighbor, path)

        return path

    def breadth_first_traversal(self, start):
        """Traverse a weighted graph breadth first."""
        if start not in self._gdict:
            raise KeyError(start, "not in graph.")
        path = []
        q = Queue()
        q.enqueue(start)

        while len(q) > 0:
            current = q.dequeue()
            if current not in path:
                path.append(current)

            for neighbor in list(self._gdict[current]):
                if neighbor not in path:
                    q.enqueue(neighbor)

        return path
