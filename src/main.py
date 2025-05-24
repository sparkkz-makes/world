from graph import Graph




def main():
    print("Hello from world!")
    g = Graph()
    alice = g.add_node("PERSON", "Alice", {"age": 30})
    bob = g.add_node("PERSON", "Bob", {"age": 25})
    g.add_edge(alice, bob, "KNOWS", {"since": 2020})
    g.add_edge(bob, alice, "Likes", {"since": 2021}, directed = True)

    print("Nodes in the graph:")
    for node in g.get_nodes():
        print(node)

    print("\nEdges in the graph:")
    for edge in g.get_edges():
        print(edge)

    print("\nGraph structure:")
    for node in g.get_nodes():
        print(f"{node}: {[str(edge) for edge in node.edges]}")

if __name__ == "__main__":
    main()
