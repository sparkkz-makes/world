from typing import Dict, Any, Optional
from .node import Node
from .edge import Edge

class Graph:
    def __init__(self):
        self.nodes: Dict[str, Node] = {}
        self.edges: Dict[str, Edge] = {}

    def add_node(
        self,
        label: str,
        name: str,
        properties: Optional[Dict[str, Any]] = None
    ):
        if properties is None:
            properties = {}
        node = Node(label, name, properties)
        self.nodes[node.id] = node
        return node

    def add_edge(
        self,
        source: Node,
        target: Node,
        label: str = "",
        properties: Optional[Dict[str, Any]] = None,
        directed: bool = False
    ):
        if properties is None:
            properties = {}
        edge = Edge(source, target, label, properties, directed)
        self.edges[edge.id] = edge
        return edge

    def get_nodes(self) -> list[Node]:
        return list(self.nodes.values())

    def get_edges(self) -> list[Edge]:
        return list(self.edges.values())
    
    def get_node(self, node_id: str) -> Optional[Node]:
        return self.nodes.get(node_id)
    
    def get_edge(self, edge_id: str) -> Optional[Edge]:
        return self.edges.get(edge_id)
    
    def remove_node(self, node_id: str) -> bool:
        node = self.nodes.pop(node_id, None)
        if node:
            for edge in node.edges:
                self.edges.pop(edge.id)
            return True
        return False