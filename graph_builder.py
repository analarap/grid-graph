import networkx as nx

def build_graph(grid, warehouse_ids):
    rows, cols = len(grid), len(grid[0])
    graph = nx.Graph()

    roads = set()
    buildings = {}

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell.isdigit() and cell != "0":
                building_id = int(cell)
                buildings[(r, c)] = building_id
            elif cell == "0":
                roads.add((r, c))

    for pos, building_id in buildings.items():
        graph.add_node(pos, type="building", id=building_id)

    for road in roads:
        graph.add_node(road, type="road")

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for r, c in roads:
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if (nr, nc) in roads:
                graph.add_edge((r, c), (nr, nc), weight=1)
            elif (nr, nc) in buildings:
                graph.add_edge((r, c), (nr, nc), weight=1)

    print("Nós no grafo:", list(graph.nodes))
    print("Arestas no grafo:", list(graph.edges))

    return graph
