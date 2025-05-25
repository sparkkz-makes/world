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
        source.add_edge(edge)
        target.add_edge(edge)
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
    
    def dump_node(self, node_id: str, max_fan_out: int = 10, max_nodes: int = 10, max_depth: int = 3):
        node = self.nodes.get(node_id)
        if not node:
            print(f"Node with ID {node_id} not found.")
            return
        node_count = 0
        depth = 0

        # maintain lists of printed nodes and edges to avoid infinite loops
        printed_nodes = set()  
        printed_edges = set()

        # maintain dictionaries of nodes to print for this and the next depth
        current_layer_to_print = {node.id: node}
        next_layer_to_print = {}

        for layer in range(max_depth):
            while current_layer_to_print and node_count < max_nodes:
                # pop the next node to print
                current_node_id, current_node = current_layer_to_print.popitem()
                if current_node_id in printed_nodes:
                    continue
                
                self._print_node(current_node)
                printed_nodes.add(current_node_id)

                # follow each edge from the current node
                edge_count = 0
                for edge in current_node.edges:
                    if edge_count < max_fan_out:
                        if edge.id in printed_edges:
                            continue
                        printed_edges.add(edge.id)
                        
                        if edge.start_node == current_node:
                            other_node = edge.end_node
                            arrow = "->"
                        else:
                            other_node = edge.start_node
                            arrow = "<-"
                        if not edge.directed:
                            arrow = "--"

                        self._print_edge(edge, arrow, other_node)
                        edge_count += 1
                        
                        if other_node.id not in printed_nodes:
                            next_layer_to_print[other_node.id] = other_node
                    else:
                        print(f"Reached maximum edge count of {max_fan_out} for node {current_node.name}.")
                        break
                
                node_count += 1
        
            # printed all this layer, move to the next layer
            if next_layer_to_print:
                current_layer_to_print = next_layer_to_print
                next_layer_to_print = {}
            else:
                break


    def _print_node(self, node: Node):
        print(f"{node.name}:{node.label} ({node.id}) {{{'' if node.properties else '}'}")
        if node.properties:
            for key, value in node.properties.items():
                print(f"        {key}: {value}")
            print("    }")

    def _print_edge(self, edge: Edge, arrow: str, other_node: Node):
        print(f"    {arrow} {edge.label} {other_node.name}:{other_node.label} ({other_node.id}) {{{'' if other_node.properties else '}'}")
        if edge.properties:
            for key, value in edge.properties.items():
                print(f"        {key}: {value}")
            print("    }")