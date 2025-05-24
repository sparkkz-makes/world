from graph import Graph
import shlex
import re

class Console():
    def __init__(self, graph):
        self.graph = graph
        self.commands = {
            "help": self.help,
            "exit": self.exit,
            "clear": self.clear,
        }

    def help(self):
        print("Available commands:")
        for command in self.commands.keys():
            print(f"- {command}")

    def exit(self):
        print("Exiting console...")
        exit()

    def clear(self):
        print("\033[H\033[J", end="")  # ANSI escape code to clear the console

    def run(self):
        while True:
            command = input("> ")
            if command in self.commands:
                self.commands[command]()
            elif command.startswith("CREATE"):
                self.parse_cypher_create(command)
            else:
                print("Unknown command. Type 'help' for a list of commands.")


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
        name = ""
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
            if key == "name":
                name = value

        if not name:
            print("CREATE command must include a 'name' property.")
            return

        self.graph.add_node(label, name, props)
        print(f"Node created: label={label}, name={name}, properties={props}")