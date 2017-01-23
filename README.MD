#Summary

This Repository contains python implementations of common datastructures.

[![Build Status](https://travis-ci.org/CCallahanIV/data-structures.svg?branch=master)](https://travis-ci.org/CCallahanIV/data-structures)


Implement a [Weighted Graph](https://codefellows.github.io/sea-python-401d5/assignments/graph_3_weighted.html)
in Python containing the following methods:


    * g.nodes(): return a list of all nodes in the graph
    * g.edges(): return a list of all edges in the graph
    * g.add_node(n): adds a new node 'n' to the graph
    * g.add_edge(n1, n2): adds a new edge to the graph connecting 'n1' and 'n2', if either n1 or n2 are not already present in the graph, they should be added.
    * g.del_node(n): deletes the node 'n' from the graph, raises an error if no such node exists
    * g.del_edge(n1, n2): deletes the edge connecting 'n1' and 'n2' from the graph, raises an error if no such edge exists
    * g.has_node(n): True if node 'n' is contained in the graph, False if not.
    * g.neighbors(n): returns the list of all nodes connected to 'n' by edges, raises an error if n is not in g
    * g.adjacent(n1, n2): returns True if there is an edge connecting n1 and n2, False if not, raises an error if either of the supplied nodes are not in g
    * g.depth_first_traversal(start): Returns the path list for the entire graph with a depth first traversal.
    * g.breadth_first_travers(start): Returns the path list for the entire graph with a breadth first traversal.


# Coverage:

---------- coverage: platform darwin, python 3.5.2-final-0 -----------


| Name                     | Stmts | Miss | Cover |
| -----------------------  | ----- | ---- | ----- |
| weighted_graph.py        |  78   |  3   | 96%   |
| test_weighted_graph.py   |  178  |  0   | 100%  |
| -----------------------  |  ---  |  --  | ----  |
| TOTAL                    |  256  |  3   | 98%   |


#Hash Functions:
    Additive hash:
    __init__ : O(n)
    get: O(1) + O(k)
    set: O(k) + O(1)
    _hash: O(m)

    FNV hash:
    __init__ : O(n)
    get: O(1) + O(k)
    set: O(k) + O(1)
    _hash: O(m)