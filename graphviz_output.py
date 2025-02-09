def export_to_graphviz(graph, output_filename="output_graph.dot"):
    with open(output_filename, "w") as f:
        f.write("graph G {\n")
        
        for node, data in graph.nodes(data=True):
            node_type = data.get("type", "")
            label = f"{node}" if node_type == "road" else f"{data.get('id', '?')}"
            shape = "ellipse" if node_type == "building" else "box" if node_type == "warehouse" else "circle"
            f.write(f'  "{node}" [label="{label}" shape={shape}];\n')
        
        for node1, node2, data in graph.edges(data=True):
            weight = data.get("weight", 1)
            f.write(f'  "{node1}" -- "{node2}" [label="{weight}"];\n')
        
        f.write("}\n")
