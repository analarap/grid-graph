from graph_builder import build_graph
from graphviz_output import export_to_graphviz

def load_grid(filename):
    """Carrega a grade de um arquivo de texto."""
    with open(filename, 'r') as f:
        return [list(line.strip()) for line in f.readlines()]