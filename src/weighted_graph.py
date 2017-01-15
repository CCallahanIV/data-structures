"""This module contains an implementation of a weighted graph."""

from queue_ds import Queue
from collections import OrderedDict
from math import inf

class WGraph(object):
    """Define a unidirectional, weighted graph datastructure.

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
        g.depth_first_traversal(start): Returns the path list for the entire graph with a depth first traversal.
        g.breadth_first_travers(start): Returns the path list for the entire graph with a breadth first traversal.

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
        self._gdict.setdefault(n, OrderedDict())

    def add_edge(self, n1, n2, weight=1):
        """Add a new edge to the weighted graph connecting n1 and n2."""
        if n1 == n2:
            raise KeyError("Edges cannot connect a node to itself.")
        if n1 in self._gdict and n2 in self._gdict[n1]:
            return
        if type(weight) is not int:
            raise TypeError("weight must be an integer")
        self._gdict.setdefault(n1, OrderedDict())[n2] = weight
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
        """Return a list of all neighbors of node n."""
        try:
            return list(self._gdict[n])
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

    def shortest_dijkstra(self, start, target):
        """Use Dijkstra's algorithm to find the shortest path from start to target."""
        # import pdb; pdb.set_trace()
        distance = {}
        path_weights = {start: (None, 0)}
        for key in self._gdict:
            distance[key] = inf
        distance[start] = 0

        while distance:
            curr = min(distance, key=distance.get)

            for neighbor in self._gdict[curr]:
                temp_dist = distance[curr] + self._gdict[curr][neighbor]

                if neighbor in distance and temp_dist < distance[neighbor]:
                    distance[neighbor] = temp_dist
                    path_weights[neighbor] = (curr, temp_dist)

            del distance[curr]

        path = []
        prev = target
        while prev is not None:
            path.append(prev)
            prev = path_weights[prev][0]
        return list(reversed(path))

    def shortest_floyd_warshall(self, start, target):
        """Return the shortest path as determined by the Floyd Warshall algo."""
        distance = {}
        nxt = {}
        nodes = self._gdict.keys()

        for edge in self.edges():
            distance.setdefault(edge[0], {})[edge[1]] = edge[2]
            nxt.setdefault(edge[0], {})[edge[1]] = edge[1]

        for node in nodes:
            for neighbor in nodes:
                if neighbor not in self._gdict[node]:
                    distance.setdefault(node, {})[neighbor] = inf

        for k in nodes:
            for i in nodes:
                for j in nodes:
                    if distance[i][j] > distance[i][k] + distance[k][j]:
                        distance[i][j] = distance[i][k] + distance[k][j]
                        nxt[i][j] = nxt[i][k]

        return self._return_path_floyd_warshall(start, target, nxt)

    def _return_path_floyd_warshall(self, start, target, nxt):
        """Return the shortest path from start to target given the nxt dictionary."""
        if nxt[start][target] is None:
            return []
        path = [start]
        while start is not target:
            start = nxt[start][target]
            path.append(start)
        return path
