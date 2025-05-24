from __future__ import annotations
from typing import List, Dict, Any, Optional
import uuid

class Node:
    def __init__(
        self,
        label: str,
        name: str,
        properties: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize a Node.

        Args:
            label (str): The label of the node (use as 'type' or 'class' label).
            name (str): The name of the node.
            properties (Optional[Dict[str, Any]]): Optional dictionary of properties.
        """
        self.id: str = str(uuid.uuid4())
        self.label: str = label
        self.name: str = name
        self.properties: Dict[str, Any] = properties if properties is not None else {}
        self.edges: List["Edge"] = []  # Use string annotation

    def add_edge(self, edge: "Edge") -> None:  # Use string annotation
        """Add an edge to this node."""
        self.edges.append(edge)

    def __repr__(self) -> str:
        return f"Node({self.name})"

    def __str__(self) -> str:
        return self.name

