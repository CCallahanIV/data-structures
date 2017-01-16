"""This module contains tests for the weighted graph implementation."""
"""This module contains the tests for a graph data structure."""
# Until we refactor our WGraph class to be ble to take in negative numbers, we're leaving negatives out for Floyd Warshall.

import pytest

TEST_NODES = [1, 2, 3, 4, "five", "six", "seven", "apple"]
TEST_EDGES = [(1, 2, 1), (2, 3, 2), (1, 3, 4), (3, 1, 2), (5, "six", 2), ("pear", "bear", 1)]
TRAVERSAL_NODES = ["A", "B", "C", "D", "E", "F", "G"]
TRAVERSAL_EDGES = [("A", "B", 1), ("A", "C", 1), ("B", "D", 1), ("B", "E", 1), ("C", "F", 1), ("C", "G", 1)]
CYCLICAL_NODES = [1, 2, 3]
CYCLICAL_EDGES = [(1, 2, 1), (2, 3, 1), (3, 1, 2)]
MED_CYCLICAL_NODES = [1, 2, 3, 4, 5, 6, 7]
MED_CYCLICAL_EDGES = [(1, 2, 1), (2, 3, 1), (3, 4, 2), (4, 5, 3), (5, 6, 4), (6, 7, 5), (7, 1, 6)]
COMPLEX_TRAVERSAL_NODES = [1, 2, 3, 4, 5, 6, 7, 8, 9]
COMPLEX_TRAVERSAL_EDGES = [(1, 3, 2), (1, 7, 3), (2, 4, 1), (2, 8, 4), (3, 6, 1), (3, 2, 1), (4, 5, 1), (4, 1, 1), (4, 9, 1), (5, 8, 1), (5, 2, 1), (5, 9, 1), (6, 3, 1), (6, 8, 1), (6, 5, 1), (7, 3, 1), (7, 1, 1), (7, 8, 1), (8, 1, 1), (8, 3, 1), (8, 5, 1), (8, 7, 1), (9, 2, 1), (9, 4, 1), (9, 6, 1)]
CIRCLE_WITH_TAIL_NODES = [1, 3, 2, 4, 5, 6]
CIRCLE_WITH_TAIL_EDGES = [(1, 2, 1), (2, 4, 1), (2, 3, 2), (3, 1, 3), (4, 5, 4), (5, 6, 5)]

@pytest.fixture
def empty_graph():
    """Create an empty graph."""
    from weighted_graph import WGraph
    return WGraph()


@pytest.fixture
def graph_nodes():
    from weighted_graph import WGraph
    g = WGraph()
    for node in TEST_NODES:
        g.add_node(node)
    return g


@pytest.fixture
def graph_edges():
    from weighted_graph import WGraph
    g = WGraph()
    for node in TEST_NODES:
        g.add_node(node)

    for edge in TEST_EDGES:
        g.add_edge(edge[0], edge[1], edge[2])
    return g


@pytest.fixture
def traversal_graph():
    from weighted_graph import WGraph
    tg = WGraph()
    for node in TRAVERSAL_NODES:
        tg.add_node(node)
    for edge in TRAVERSAL_EDGES:
        tg.add_edge(edge[0], edge[1], edge[2])
    return tg


@pytest.fixture
def cyclical_graph():
    from weighted_graph import WGraph
    cg = WGraph()
    for node in CYCLICAL_NODES:
        cg.add_node(node)
    for edge in CYCLICAL_EDGES:
        cg.add_edge(edge[0], edge[1], edge[2])
    return cg


@pytest.fixture
def med_cyclical_graph():
    from weighted_graph import WGraph
    mcg = WGraph()
    for node in MED_CYCLICAL_NODES:
        mcg.add_node(node)
    for edge in MED_CYCLICAL_EDGES:
        mcg.add_edge(edge[0], edge[1], edge[2])
    return mcg


@pytest.fixture
def complex_traversal_graph():
    from weighted_graph import WGraph
    ctg = WGraph()
    for node in COMPLEX_TRAVERSAL_NODES:
        ctg.add_node(node)
    for edge in COMPLEX_TRAVERSAL_EDGES:
        ctg.add_edge(edge[0], edge[1], edge[2])
    return ctg


@pytest.fixture
def circle_with_tail_graph():
    from weighted_graph import WGraph
    cwtg = WGraph()
    for node in CIRCLE_WITH_TAIL_NODES:
        cwtg.add_node(node)
    for edge in CIRCLE_WITH_TAIL_EDGES:
        cwtg.add_edge(edge[0], edge[1], edge[2])
    return cwtg

@pytest.fixture
def simple_wgraph():
    from weighted_graph import WGraph
    wg = WGraph()
    for edge in SIMPLE_WGRAPH:
        wg.add_edge(edge[0], edge[1], edge[2])
    return wg


# def test_init_graph(empty_graph):
#     """Test initialization of an empty graph."""
#     assert empty_graph._gdict == {}


# def test_nodes_returns_empty_list_empty_graph(empty_graph):
#     """Test nodes() returns empty list for an empty graph."""
#     assert empty_graph.nodes() == []


# def test_nodes_returns_list_non_empty_graph(graph_nodes):
#     """Test nodes() returns correct list."""
#     node_list = graph_nodes.nodes()
#     for node in node_list:
#         assert node in TEST_NODES
#     assert len(node_list) == len(TEST_NODES)


# def test_add_node_creates_new_node(empty_graph):
#     """Test add_node() creates a new node."""
#     g = empty_graph
#     g.add_node(1)
#     assert g._gdict[1] == {}


# def test_add_node_already_exists(empty_graph):
#     """Test adding a node that already exists."""
#     empty_graph.add_node(1)
#     empty_graph.add_node(1)
#     assert empty_graph._gdict[1] == {}


# def test_add_edge_create_new_edge_no_weight(empty_graph):
#     """Test Adding an edge to an empty graph."""
#     empty_graph.add_edge("dog", "cat")
#     assert "dog", "cat" in empty_graph._gict.keys()
#     assert empty_graph._gdict["dog"] == {"cat": 1}
#     assert empty_graph._gdict["dog"]["cat"] == 1


# def test_add_edge_create_new_edge_with_weight(empty_graph):
#     """Test Adding an edge to an empty graph."""
#     empty_graph.add_edge("dog", "cat", 3)
#     assert "dog", "cat" in empty_graph._gict.keys()
#     assert empty_graph._gdict["dog"] == {"cat": 3}
#     assert empty_graph._gdict["dog"]["cat"] == 3


# def test_add_edge_non_int_weight_raises_error(empty_graph):
#     """Test that creating an edge with a non-integer weight raises an error."""
#     with pytest.raises(TypeError):
#         empty_graph.add_edge("dog", "cat", "turtle")


# def test_add_edge_n1_already_exists(graph_edges):
#     """Test adding an edge where n1 already exsists."""
#     graph_edges.add_edge(1, "grapple")
#     assert "grapple" in graph_edges._gdict[1]
#     assert "grapple" in graph_edges.nodes()


# def test_add_edge_n1_does_not_exist_n2_does(graph_edges):
#     """Test case where n1 does not exist, n2 does."""
#     graph_edges.add_edge("grapple", 1)
#     assert 1 in graph_edges._gdict["grapple"]
#     assert "grapple" in graph_edges.nodes()


# def test_add_edge_already_exists(graph_edges):
#     """Testing adding an edge to a graph already with that edge, doesn't change it."""
#     old_edges = graph_edges._gdict[1]
#     graph_edges.add_edge(1, 2)
#     assert old_edges == graph_edges._gdict[1]


# def test_del_node_deletes_node_and_all_points_to_node(graph_edges):
#     """Test that del_node() delets the node and all pointers to that node."""
#     graph_edges.del_node(3)
#     assert 3 not in graph_edges.nodes()
#     for edge in graph_edges.edges():
#         assert 3 != edge[1]


# def test_del_node_doesnt_exist_raises_keyerror(graph_edges):
#     """Test that del_node() raises an error if node does not exist."""
#     with pytest.raises(KeyError):
#         graph_edges.del_node("widgets")


# def test_del_edge_raise_key_error_no_n1(graph_edges):
#     """Test that del_edge() raises key error if n1 does not exist."""
#     with pytest.raises(KeyError):
#         graph_edges.del_edge("widgets", "anything")


# def test_del_edge_raise_value_error_no_n2(graph_edges):
#     """Test that del edge raises a value error if n2 does not exist."""
#     with pytest.raises(KeyError):
#         graph_edges.del_edge(1, "widgets")


# def test_del_edge_functions_correctly(graph_edges):
#     """Test that del edge functions correctly."""
#     graph_edges.del_edge(1, 2)
#     assert 2 not in graph_edges._gdict[1]
#     graph_edges.del_edge(1, 3)
#     assert 3 not in graph_edges._gdict[1]
#     assert len(graph_edges._gdict[1]) == 0


# def test_has_node_return_false(graph_edges):
#     """Test that has_node() returns false if node doesn't exist."""
#     assert graph_edges.has_node("widgets") is False
#     graph_edges.del_node(1)
#     assert graph_edges.has_node(1) is False


# def test_has_node_return_true(graph_edges):
#     """Test that has_node returns True if node exists."""
#     assert graph_edges.has_node(1) is True
#     graph_edges.add_node("widgets")
#     assert graph_edges.has_node("widgets") is True


# def test_adjacent_returns_true(graph_edges):
#     """Test that adjacent() returns true if given nodes are neighbors."""
#     assert graph_edges.adjacent(1, 2) is True
#     graph_edges.add_edge(1, 5)
#     assert graph_edges.adjacent(1, 5) is True
#     assert graph_edges.adjacent(5, "six") is True


# def test_adjacent_returns_false(graph_edges):
#     """Test that adjacent() returns false if given nodes are not neighbors."""
#     assert graph_edges.adjacent(1, 5) is False
#     graph_edges.del_node(2)
#     with pytest.raises(KeyError):
#         graph_edges.adjacent(1, 2)


# def test_adjacent_raises_error_if_n_not_in_graph(graph_edges):
#     """Test that adjacent() raises an error if nodes not in graph."""
#     with pytest.raises(KeyError):
#         graph_edges.adjacent(0, 1)

#     with pytest.raises(KeyError):
#         graph_edges.adjacent(1, 0)

#     with pytest.raises(KeyError):
#         graph_edges.adjacent("widget", "gizmo")


# def test_neighbors_returns_correct_list(graph_edges):
#     """Test that neighbors returns correct list."""
#     assert graph_edges.neighbors(1) == [2, 3]
#     graph_edges.add_edge(1, 5)
#     assert graph_edges.neighbors(1) == [2, 3, 5]


# def test_nieghbors_raises_key_error_no_node(graph_edges):
#     """Test that neighbros raises a key error if the node does not exist."""
#     with pytest.raises(KeyError):
#         graph_edges.neighbors("widget")


# """Test traversal of graph."""


# def test_depth_traversal_of_simple_tree_graph_a_to_g(traversal_graph):
#     """The module tests depth traversal of graph."""
#     assert traversal_graph.depth_first_traversal("A") == ["A", "B", "D", "E", "C", "F", "G"]


# def test_depth_traversal_of_cyclical_graph(cyclical_graph):
#     """The module tests depth traversal of a cyclical graph: 1 to 2, 2 to 3, 3 to 1."""
#     assert cyclical_graph.depth_first_traversal(1) == [1, 2, 3]


# def test_breadth_traversal_of_simple_tree_graph_a_to_g(traversal_graph):
#     """The module tests breadth traversal of graph."""
#     assert traversal_graph.breadth_first_traversal("A") == ["A", "B", "C", "D", "E", "F", "G"]


# def test_breadth_traversal_of_medium_cyclical_graph(med_cyclical_graph):
#     """The module tests breadth traversal of a cyclical graph: 1 to 7."""
#     assert med_cyclical_graph.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7]


# def test_breadth_traversal_of_complex_graph(complex_traversal_graph):
#     """The module tests the breadth traversal of a complex graph."""
#     assert complex_traversal_graph.breadth_first_traversal(1) == [1, 3, 7, 6, 2, 8, 5, 4, 9]


# def test_breadth_traversal_of_circle_with_tail(circle_with_tail_graph):
#     """Test breadth traversal on a circle with a tail."""
#     assert circle_with_tail_graph.breadth_first_traversal(1) == [1, 2, 4, 3, 5, 6]


# def test_depth_traversal_of_circle_with_tail(circle_with_tail_graph):
#     """Test breadth traversal on a circle with a tail."""
#     assert circle_with_tail_graph.breadth_first_traversal(1) == [1, 2, 4, 3, 5, 6]

# # TEST SHORTEST PATHS HERE

SIMPLE_WGRAPH = [("A", "B", 3), ("A", "D", 4), ("B", "C", 2), ("B", "E", 5), ("C", "D" ,1), ("C", "G", 6), ("D","E",3), ("D","B",4), ("E","G",5), ("E","C",2), ("E","F",5), ("F","G",2)]
BASIC_WGRAPH = [("A", "C", 3), ("A", "D", 0), ("B", "A", 1), ("B", "D", 1), ("C", "D", 1), ("D", "B", 4)]
COMPLEX_WGRAPH = [("A", "B", 3), ("A", "D", 4), ("B", "C", 2), ("B", "E", 5), ("C", "D" ,1), ("C", "G", 6), ("D","E",3), ("D","B",4), ("E","G",5), ("E","C",2), ("E","F",5), ("F","G",2), ("F","D",2), ("G","D",2), ("C","A",3), ("G","F",2), ("G","B",3), ("G","A",0), ("C","E",1), ("G","C",0), ("F","C",2)]
# ALL_NEGATIVE_WGRAPH = [("A", "B", -3), ("A", "D", -4), ("B", "C", -2), ("B", "E", -5), ("C", "D" ,-1), ("C", "G", -6), ("D","E",-3), ("D","B",-4), ("E","G",-5), ("E","C",-2), ("E","F",-5), ("F","G",-2)]


@pytest.fixture
def simple_wgraph():
    """Fixture to seet up a simple weighted-graph for use in testing."""
    from weighted_graph import WGraph
    wg = WGraph()
    for edge in SIMPLE_WGRAPH:
        wg.add_edge(edge[0], edge[1], edge[2])
    return wg

@pytest.fixture
def basic_wgraph():
    """Fixture to seet up a basic weighted-graph for use in testing."""
    from weighted_graph import WGraph
    wg = WGraph()
    for edge in BASIC_WGRAPH:
        wg.add_edge(edge[0], edge[1], edge[2])
    return wg

@pytest.fixture
def complex_wgraph():
    """Fixture to seet up a complex  weighted-graph for use in testing."""
    from weighted_graph import WGraph
    wg = WGraph()
    for edge in COMPLEX_WGRAPH:
        wg.add_edge(edge[0], edge[1], edge[2])
    return wg

# Until we refactor our WGraph class to be ble to take in negative numbers, we're leaving negatives out.

# @pytest.fixture
# def all_negative_wgraph():
#     """Fixture to seet up an all negative weighted-graph for use in testing."""
#     from weighted_graph import WGraph
#     wg = WGraph()
#     for edge in ALL_NEGATIVE_WGRAPH:
#         wg.add_edge(edge[0], edge[1], edge[2])
#     return wg



def test_dijkstra_shortest_path(simple_wgraph):
    """Test dijkstra shortest path."""
    assert simple_wgraph.shortest_dijkstra("A", "G") == ["A", "B", "C", "G"]


def test_dijkstra_shortest_path_a_to_g(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, A to G."""
    assert simple_wgraph.shortest_dijkstra("A", "G") == ["A", "B", "C", "G"]


def test_dijkstra_shortest_path_b_to_d(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, B to D."""
    assert simple_wgraph.shortest_dijkstra("B", "D") == ["B", "C", "D"]


def test_dijkstra_shortest_path_a_to_f(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, A to F."""
    assert simple_wgraph.shortest_dijkstra("A", "F") == ["A", "D", "E", "F"]


def test_dijkstra_shortest_path_d_to_c(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, D to C."""
    assert simple_wgraph.shortest_dijkstra("D", "C") == ["D", "E", "C"]


def test_dijkstra_shortest_path_d_to_g(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, D to G."""
    assert simple_wgraph.shortest_dijkstra("D", "G") == ["D", "E", "G"]


def test_dijkstra_shortest_path_d_to_f(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, D to F."""
    assert simple_wgraph.shortest_dijkstra("D", "F") == ["D", "E", "F"]


def test_dijkstra_shortest_path_e_to_b(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, E to B."""
    assert simple_wgraph.shortest_dijkstra("E", "B") == ["E", "C", "D", "B"]


def test_dijkstra_shortest_path_e_to_d(simple_wgraph):
    """Test the Dijkstra shortest path for simple graph, E to D."""
    assert simple_wgraph.shortest_dijkstra("E", "D") == ["E", "C", "D"]

# complex_wgraph

def test_dijkstra_shortest_path_a_to_g_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, A to G."""
    assert complex_wgraph.shortest_dijkstra("A", "G") == ["A", "B", "C", "G"]


def test_dijkstra_shortest_path_b_to_d_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, B to D."""
    assert complex_wgraph.shortest_dijkstra("B", "D") == ["B", "C", "D"]


def test_dijkstra_shortest_path_a_to_f_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, A to F."""
    assert complex_wgraph.shortest_dijkstra("A", "F") == ["A", "B", "C", "E", "F"]


def test_dijkstra_shortest_path_d_to_c_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, D to C."""
    assert complex_wgraph.shortest_dijkstra("D", "C") == ["D", "E", "C"]


def test_dijkstra_shortest_path_d_to_g_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, D to G."""
    assert complex_wgraph.shortest_dijkstra("D", "G") == ["D", "E", "G"]


def test_dijkstra_shortest_path_d_to_f_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, D to F."""
    assert complex_wgraph.shortest_dijkstra("D", "F") == ["D", "E", "F"]


def test_dijkstra_shortest_path_e_to_b_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, E to B."""
    assert complex_wgraph.shortest_dijkstra("E", "B") == ["E", "C", "D", "B"]


def test_dijkstra_shortest_path_e_to_d_complex(complex_wgraph):
    """Test the Dijkstra shortest path for complex graph, E to D."""
    assert complex_wgraph.shortest_dijkstra("E", "D") == ["E", "C", "D"]


# basic_wgraph

def test_dijkstra_shortest_path_a_to_b_basic(basic_wgraph):
    """Test the Dijkstra shortest path for basic graph, A to B."""
    assert basic_wgraph.shortest_dijkstra("A", "B") == ["A", "D", "B"]


def test_dijkstra_shortest_path_b_to_c_basic(basic_wgraph):
    """Test the Dijkstra shortest path for basic graph, B to C."""
    assert basic_wgraph.shortest_dijkstra("B", "C") == ["B", "A", "C"]


def test_dijkstra_shortest_path_d_to_c_basic(basic_wgraph):
    """Test the Dijkstra shortest path for basic graph, D to C."""
    assert basic_wgraph.shortest_dijkstra("D", "C") == ["D", "B", "A", "C"]


def test_dijkstra_shortest_path_c_to_a_basic(basic_wgraph):
    """Test the Dijkstra shortest path for basic graph, C to A."""
    assert basic_wgraph.shortest_dijkstra("C", "A") == ["C", "D", "B", "A"]


def test_dijkstra_shortest_path_c_to_b_basic(basic_wgraph):
    """Test the Dijkstra shortest path for basic graph, C to B."""
    assert basic_wgraph.shortest_dijkstra("C", "B") == ["C", "D", "B"]


def test_floyd_warshall_shortest_path_a_to_g(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, A to G."""
    assert simple_wgraph.shortest_floyd_warshall("A", "G") == ["A", "B", "C", "G"]


def test_floyd_warshall_shortest_path_b_to_d(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, B to D."""
    assert simple_wgraph.shortest_floyd_warshall("B", "D") == ["B", "C", "D"]


def test_floyd_warshall_shortest_path_a_to_f(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, A to F."""
    assert simple_wgraph.shortest_floyd_warshall("A", "F") == ["A", "D", "E", "F"]


def test_floyd_warshall_shortest_path_d_to_c(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, D to C."""
    assert simple_wgraph.shortest_floyd_warshall("D", "C") == ["D", "E", "C"]


def test_floyd_warshall_shortest_path_d_to_g(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, D to G."""
    assert simple_wgraph.shortest_floyd_warshall("D", "G") == ["D", "E", "G"]


def test_floyd_warshall_shortest_path_d_to_f(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, D to F."""
    assert simple_wgraph.shortest_floyd_warshall("D", "F") == ["D", "E", "F"]


def test_floyd_warshall_shortest_path_e_to_b(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, E to B."""
    assert simple_wgraph.shortest_floyd_warshall("E", "B") == ["E", "C", "D", "B"]


def test_floyd_warshall_shortest_path_e_to_d(simple_wgraph):
    """Test the floyd Warshall shortest path for simple graph, E to D."""
    assert simple_wgraph.shortest_floyd_warshall("E", "D") == ["E", "C", "D"]

# complex_wgraph

def test_floyd_warshall_shortest_path_a_to_g_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, A to G."""
    assert complex_wgraph.shortest_floyd_warshall("A", "G") == ["A", "B", "C", "G"]


def test_floyd_warshall_shortest_path_b_to_d_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, B to D."""
    assert complex_wgraph.shortest_floyd_warshall("B", "D") == ["B", "C", "D"]


def test_floyd_warshall_shortest_path_a_to_f_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, A to F."""
    assert complex_wgraph.shortest_floyd_warshall("A", "F") == ["A", "B", "C", "E", "F"]


def test_floyd_warshall_shortest_path_d_to_c_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, D to C."""
    assert complex_wgraph.shortest_floyd_warshall("D", "C") == ["D", "E", "C"]


def test_floyd_warshall_shortest_path_d_to_g_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, D to G."""
    assert complex_wgraph.shortest_floyd_warshall("D", "G") == ["D", "E", "G"]


def test_floyd_warshall_shortest_path_d_to_f_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, D to F."""
    assert complex_wgraph.shortest_floyd_warshall("D", "F") == ["D", "E", "F"]


def test_floyd_warshall_shortest_path_e_to_b_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, E to B."""
    assert complex_wgraph.shortest_floyd_warshall("E", "B") == ["E", "C", "D", "B"]


def test_floyd_warshall_shortest_path_e_to_d_complex(complex_wgraph):
    """Test the floyd Warshall shortest path for complex graph, E to D."""
    assert complex_wgraph.shortest_floyd_warshall("E", "D") == ["E", "C", "D"]


# basic_wgraph

def test_floyd_warshall_shortest_path_a_to_b_basic(basic_wgraph):
    """Test the floyd Warshall shortest path for basic graph, A to B."""
    assert basic_wgraph.shortest_floyd_warshall("A", "B") == ["A", "D", "B"]


def test_floyd_warshall_shortest_path_b_to_c_basic(basic_wgraph):
    """Test the floyd Warshall shortest path for basic graph, B to C."""
    assert basic_wgraph.shortest_floyd_warshall("B", "C") == ["B", "A", "C"]


def test_floyd_warshall_shortest_path_d_to_c_basic(basic_wgraph):
    """Test the floyd Warshall shortest path for basic graph, D to C."""
    assert basic_wgraph.shortest_floyd_warshall("D", "C") == ["D", "B", "A", "C"]


def test_floyd_warshall_shortest_path_c_to_a_basic(basic_wgraph):
    """Test the floyd Warshall shortest path for basic graph, C to A."""
    assert basic_wgraph.shortest_floyd_warshall("C", "A") == ["C", "D", "B", "A"]


def test_floyd_warshall_shortest_path_c_to_b_basic(basic_wgraph):
    """Test the floyd Warshall shortest path for basic graph, C to B."""
    assert basic_wgraph.shortest_floyd_warshall("C", "B") == ["C", "D", "B"]

# all_negative_wgraph
# Until we refactor our WGraph class to be ble to take in negative numbers, we're leaving negatives out.

# def test_floyd_warshall_shortest_path_a_to_g_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, A to G."""
#     assert all_negative_wgraph.shortest_floyd_warshall("A", "G") == ["A", "C", "G"]


# def test_floyd_warshall_shortest_path_b_to_d_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, B to D."""
#     assert all_negative_wgraph.shortest_floyd_warshall("B", "D") == ["B", "C", "D"]


# def test_floyd_warshall_shortest_path_a_to_f_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, A to F."""
#     assert all_negative_wgraph.shortest_floyd_warshall("A", "F") == ["A", "C", "F"]


# def test_floyd_warshall_shortest_path_d_to_c_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, d to c."""
#     assert all_negative_wgraph.shortest_floyd_warshall("D", "C") == ["D", "C", "C"]


# def test_floyd_warshall_shortest_path_d_to_g_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, d to g."""
#     assert all_negative_wgraph.shortest_floyd_warshall("D", "G") == ["D", "C", "G"]


# def test_floyd_warshall_shortest_path_d_to_f_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, d to f."""
#     assert all_negative_wgraph.shortest_floyd_warshall("D", "F") == ["D", "C", "F"]


# def test_floyd_warshall_shortest_path_e_to_b_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, e to b."""
#     assert all_negative_wgraph.shortest_floyd_warshall("E", "B") == ["E", "C", "B"]


# def test_floyd_warshall_shortest_path_e_to_d_all_negative(all_negative_wgraph):
#     """Test the floyd Warshall shortest path for all negative graph, e to d."""
#     assert all_negative_wgraph.shortest_floyd_warshall("E", "D") == ["E", "C", "D"]
