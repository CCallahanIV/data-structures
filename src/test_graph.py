"""This module contains the tests for a graph data structure."""

import pytest

TEST_NODES = [1, 2, 3, 4, "five", "six", "seven", "apple"]
TEST_EDGES = [(1, 2), (2, 3), (3, 1), (5, "six"), ("pear", "bear")]


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
        g.add_edge(edge)
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
