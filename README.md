# Grid-Graph
A project that converts a 200x200 grid of buildings, roads, and empty spaces into a weighted graph, enabling the visualization of road connections between buildings.

### How Execute

1. Clone this repository:
   
```bash
   git clone https://github.com/analarap/grid-graph.git
```

2. Install dependencies:
   
```bash
   pip install -r requirements.txt
```

3. Run the main script:
   
```bash
   python main.py
```

4. The file `output_graph.dot` will be generated. To generate the png file, execute on terminal:
   
```bash
   dot -Tpng output_graph.dot -o output_graph.png
```

5. Open `output_graph.png` to see the graph.

### Tecnologies
- **Python** (for graph manipulation)
- **Graphviz** (for graph visualization)

### Notes
- The grid can be personalizate on file example_grid.txt.
- Make sure Graphviz is installed on your system:
   ```bash
   sudo apt install graphviz  # Linux
   brew install graphviz      # macOS
   choco install graphviz     # Windows (Chocolatey)
   ```
   Alternatively, you can manually download and install Graphviz from this link: https://graphviz.org/download/

#

Thanks!

#
