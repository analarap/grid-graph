from graph_builder import build_graph
from graphviz_output import export_to_graphviz

def load_grid(filename):
    with open(filename, "r") as f:
        grid = [list(line.strip()) for line in f.readlines() if line.strip()]
    return grid

def main():
    grid = load_grid("example_grid.txt")
    warehouse_ids = {"A", "B"}
    graph = build_graph(grid, warehouse_ids)
    export_to_graphviz(graph, "output_graph.dot")
    print("Grafo gerado com sucesso! Veja o arquivo output_graph.dot")

if __name__ == "__main__":
    main()