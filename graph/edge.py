from __future__ import annotations
from typing import Optional, Dict, Any
import uuid
from .node import Node


class Edge:
    def __init__(
        self,
        start_node: Node,
        end_node: Node,
        label: str,
        properties: Optional[Dict[str, Any]] = None,
        directed: bool = False
    ):
        self.id: str = str(uuid.uuid4())
        self.start_node: Node = start_node
        self.end_node: Node = end_node
        self.label: str = label
        self.directed: bool = directed
        self.properties: Dict[str, Any] = properties if properties is not None else {}

    def __repr__(self) -> str:
        return f"Edge({self.start_node}, {self.end_node}, '{self.label}', directed={self.directed}, properties={self.properties})"
    
    def __str__(self) -> str:
        return f"{self.start_node} --{self.label}--> {self.end_node}" if self.directed else f"{self.start_node} --{self.label}-- {self.end_node}"
    
