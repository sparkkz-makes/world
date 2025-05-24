import pytest
from src.graph import Graph

def test_graph_initialization():
    graph = Graph()
    assert graph.nodes == {}
    assert graph.edges == {}

def test_add_node():
    graph = Graph()
    node = graph.add_node("PERSON", "Alice", {"age": 30})
    assert len(graph.nodes) == 1
    assert graph.nodes[node.id] == node
    assert node.label == "PERSON"
    assert node.name == "Alice"
    assert node.properties == {"age": 30}
