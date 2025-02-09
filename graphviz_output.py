def export_to_graphviz(graph, filename):
    """Exporta o grafo para um arquivo Graphviz DOT."""
    with open(filename, "w") as f:
        f.write("graph G {\n")
        for node, edges in graph.items():
            for neighbor, weight in edges:
                f.write(f"    {node} -- {neighbor} [label=\"{weight}\"];\n")
        f.write("}\n")