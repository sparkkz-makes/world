from graph import Graph
from console import Console
import datetime




def main():
    print("Hello from world!")
    g = Graph()
    megan = g.add_node("Person", "Megan", {"born": datetime.date(1966, 2, 20)})
    stuart = g.add_node("Person", "Stuart", {"born": datetime.date(1966, 9, 27)})
    lorraine = g.add_node("Person", "Lorraine")
    neil = g.add_node("Person", "Neil")
    mike = g.add_node("Person", "Mike", {"born": datetime.date(1935, 3, 7), "died": datetime.date(2020, 3, 10)})
    pamela = g.add_node("Person", "Pamela", {"born": datetime.date(1938, 3, 24)})
    invercargill = g.add_node("Place", "Invercargill", {"country": "NZ", "province": "Southland"})
    g.add_edge(megan, invercargill, "LIVES_IN", {"since": 2022}, directed=True)
    g.add_edge(stuart, invercargill, "LIVES_IN", {"since": 2022}, directed=True)
    g.add_edge(stuart, megan, "MARRIED_TO", {"since": 1995})
    g.add_edge(lorraine, megan, "MOTHER_OF", directed=True)
    g.add_edge(lorraine, neil, "MARRIED_TO", {"since": 1990})
    g.add_edge(neil, megan, "FATHER_OF", directed=True)

    print("Nodes in the graph:")
    for node in g.get_nodes():
        print(node)

    print("\nEdges in the graph:")
    for edge in g.get_edges():
        print(edge)

    print("\nGraph structure:")
    for node in g.get_nodes():
        print(f"{node}: {[str(edge) for edge in node.edges]}")

    print("\nDumping node 'Megan':\n---------------------------")
    g.dump_node(megan.id, max_fan_out=10, max_nodes=10, max_depth=4)

    # c = Console(g)
    # c.run()

if __name__ == "__main__":
    main()
