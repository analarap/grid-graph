def build_graph(grid, warehouse_ids):
    """Transforma a grade em um grafo onde os vértices representam interseções de estradas e prédios."""
    graph = {}
    rows, cols = len(grid), len(grid[0])
    
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "#":
                graph[(r, c)] = []
                for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "#":
                        graph[(r, c)].append(((nr, nc), 1))
    
    return graph