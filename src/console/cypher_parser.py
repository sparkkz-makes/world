


class Cypher_Parser():
    def __init__(self, graph):
        self.graph = graph
        self.variables = {}

    def parse_cypher_create(self, command: str):
        """
        Parses a simple Cypher CREATE command like:
        CREATE (n:Person {name: "Alice", age: 30})
        and calls add_node with label, name, and properties.
        """
        pattern = r'CREATE\s*\((\w*):(\w+)\s*\{([^}]*)\}\)'
        match = re.match(pattern, command.strip(), re.IGNORECASE)
        if not match:
            print("Invalid CREATE command format.")
            return

        name = match.group(1)
        label = match.group(2)
        props_str = match.group(3)

        # Parse properties: key: value pairs
        props = {}
        for prop in re.finditer(r'(\w+)\s*:\s*("[^"]*"|\d+)', props_str):
            key = prop.group(1)
            value = prop.group(2)
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            else:
                try:
                    value = int(value)
                except ValueError:
                    pass
            props[key] = value

        # Add node to graph
        node = self.graph.add_node(label, name, props)
        self.variables[name] = node

