"""This module contains the tests for a graph data structure."""

import pytest

TEST_NODES = [1, 2, 3, 4, "five", "six", "seven", "apple"]
TEST_EDGES = [(1, 2), (2, 3), (1, 3), (3, 1), (5, "six"), ("pear", "bear")]


@pytest.fixture
def empty_graph():
    """Create an empty graph."""
    from graph import Graph
    return Graph()


@pytest.fixture
def graph_nodes():
    from graph import Graph
    g = Graph()
    for node in TEST_NODES:
        g.add_node(node)
    return g


@pytest.fixture
def graph_edges():
    from graph import Graph
    g = Graph()
    for node in TEST_NODES:
        g.add_node(node)

    for edge in TEST_EDGES:
        g.add_edge(edge[0], edge[1])
    return g


def test_init_graph(empty_graph):
    """Test initialization of an empty graph."""
    assert empty_graph._gdict == {}


def test_nodes_returns_empty_list_empty_graph(empty_graph):
    """Test nodes() returns empty list for an empty graph."""
    assert empty_graph.nodes() == []


def test_nodes_returns_list_non_empty_graph(graph_nodes):
    """Test nodes() returns correct list."""
    node_list = graph_nodes.nodes()
    for node in node_list:
        assert node in TEST_NODES
    assert len(node_list) == len(TEST_NODES)


def test_add_node_creates_new_node(empty_graph):
    """Test add_node() creates a new node."""
    g = empty_graph
    g.add_node(1)
    assert g._gdict[1] == []


def test_add_node_already_exists(empty_graph):
    """Test adding a node that already exists."""
    empty_graph.add_node(1)
    empty_graph.add_node(1)
    assert empty_graph._gdict[1] == []


def test_add_edge_create_new_edge(empty_graph):
    """Test Adding an edge to an empty graph."""
    empty_graph.add_edge("dog", "cat")
    assert "dog", "cat" in empty_graph._gict.keys()
    assert empty_graph._gdict["dog"] == ["cat"]


def test_add_edge_n1_already_exists(graph_edges):
    """Test adding an edge where n1 already exsists."""
    graph_edges.add_edge(1, "grapple")
    assert "grapple" in graph_edges._gdict[1]
    assert "grapple" in graph_edges.nodes()


def test_add_edge_n1_does_not_exist_n2_does(graph_edges):
    """Test case where n1 does not exist, n2 does."""
    graph_edges.add_edge("grapple", 1)
    assert 1 in graph_edges._gdict["grapple"]
    assert "grapple" in graph_edges.nodes()


def test_add_edge_already_exists(graph_edges):
    """Testing adding an edge to a graph already with that edge, doesn't change it."""
    old_edges = graph_edges._gdict[1]
    graph_edges.add_edge(1, 2)
    assert old_edges == graph_edges._gdict[1]


def test_del_node_deletes_node_and_all_points_to_node(graph_edges):
    """Test that del_node() delets the node and all pointers to that node."""
    graph_edges.del_node(3)
    assert 3 not in graph_edges.nodes()
    for edge in graph_edges.edges():
        assert 3 != edge[1]


def test_del_node_doesnt_exist_raises_keyerror(graph_edges):
    """Test that del_node() raises an error if node does not exist."""
    with pytest.raises(KeyError):
        graph_edges.del_node("widgets")


def test_del_edge_raise_key_error_no_n1(graph_edges):
    """Test that del_edge() raises key error if n1 does not exist."""
    with pytest.raises(KeyError):
        graph_edges.del_edge("widgets", "anything")


def test_del_edge_raise_value_error_no_n2(graph_edges):
    """Test that del edge raises a value error if n2 does not exist."""
    with pytest.raises(ValueError):
        graph_edges.del_edge(1, "widgets")


def test_del_edge_functions_correctly(graph_edges):
    """Test that del edge functions correctly."""
    graph_edges.del_edge(1, 2)
    assert 2 not in graph_edges._gdict[1]
    graph_edges.del_edge(1, 3)
    assert 3 not in graph_edges._gdict[1]
    assert len(graph_edges._gdict[1]) == 0


def test_has_node_return_false(graph_edges):
    """Test that has_node() returns false if node doesn't exist."""
    assert graph_edges.has_node("widgets") is False
    graph_edges.del_node(1)
    assert graph_edges.has_node(1) is False


def test_has_node_return_true(graph_edges):
    """Test that has_node returns True if node exists."""
    assert graph_edges.has_node(1) is True
    graph_edges.add_node("widgets")
    assert graph_edges.has_node("widgets") is True


def test_adjacent_returns_true(graph_edges):
    """Test that adjacent() returns true if given nodes are neighbors."""
    assert graph_edges.adjacent(1, 2) is True
    graph_edges.add_edge(1, 5)
    assert graph_edges.adjacent(1, 5) is True
    assert graph_edges.adjacent(5, "six") is True


def test_adjacent_returns_false(graph_edges):
    """Test that adjacent() returns false if given nodes are not neighbors."""
    assert graph_edges.adjacent(1, 5) is False
    graph_edges.del_node(2)
    assert graph_edges.adjacent(1, 2) is False


def test_adjacent_raises_error_if_n_not_in_graph(graph_edges):
    """Test that adjacent() raises an error if nodes not in graph."""
    with pytest.raises(KeyError):
        graph_edges.adjacent(0, 1)

    with pytest.raises(KeyError):
        graph_edges.adjacent(1, 0)

    with pytest.raises(KeyError):
        graph_edges.adjacent("widget", "gizmo")


def test_neighbors_returns_correct_list(graph_edges):
    """Test that neighbors returns correct list."""
    assert graph_edges.neighbors(1) == [2, 3]
    graph_edges.add_edge(1, 5)
    assert graph_edges.neighbors == [2, 3, 5]


def test_nieghbors_raises_key_error_no_node(graph_edges):
    """Test that neighbros raises a key error if the node does not exist."""
    with pytest.raises(KeyError):
        graph_edges.neighbors("widget")
