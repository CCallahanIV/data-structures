"""This module contains the tests for a graph data structure."""

import pytest


@pytest.fixture
def create_graph():
    """Create an empty graph."""
    from graph import Graph
    return Graph()


def test_init_graph(create_graph):
    """Test initialization of an empty graph."""
    assert create_graph._gdict == {}


def test_nodes_returns_empty_list_empty_graph(create_graph):
    """Test nodes() returns empty list for an empty graph."""
    assert create_graph.nodes() == []
