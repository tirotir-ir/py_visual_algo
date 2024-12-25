import networkx as nx
import matplotlib.pyplot as plt
from py_visual_algo.algorithms.graph import (
    bfs,
    dfs,
    dijkstra,
    a_star,
    bellman_ford,
    prim,
)

# Create the graph using NetworkX
graph_dict = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3},
}
graph = nx.Graph()
for node, neighbors in graph_dict.items():
    for neighbor, weight in neighbors.items():
        graph.add_edge(node, neighbor, weight=weight)

# Heuristic for A* (admissible values for demonstration)
heuristic = {
    "A": 7,
    "B": 6,
    "C": 2,
    "D": 1,
    "E": 0,
}


# Visualization Helper
def visualize_graph(graph, highlight_edges=None, title="Graph"):
    """
    Visualize a graph using NetworkX and matplotlib.

    Args:
        graph (nx.Graph): The graph to visualize.
        highlight_edges (list): List of edges to highlight (e.g., shortest path or MST).
        title (str): Title of the plot.
    """
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", font_weight="bold")

    # Draw all edges with default color
    nx.draw_networkx_edge_labels(
        graph,
        pos,
        edge_labels=nx.get_edge_attributes(graph, "weight"),
        font_color="red",
    )

    if highlight_edges:
        nx.draw_networkx_edges(
            graph, pos, edgelist=highlight_edges, edge_color="red", width=2
        )
    plt.title(title)
    plt.show()


# Run and Visualize BFS
bfs_result = bfs(graph_dict, start="A")
print("BFS:", bfs_result)
visualize_graph(graph, title="BFS (No Edge Highlighting)")

# Run and Visualize DFS
dfs_result = dfs(graph_dict, start="A")
print("DFS:", dfs_result)
visualize_graph(graph, title="DFS (No Edge Highlighting)")

# Run and Visualize Dijkstra's Algorithm
dijkstra_generator = dijkstra(graph_dict, start="A")
dijkstra_path = None
for node, distances in dijkstra_generator:
    print(f"Dijkstra's - Node: {node}, Distances: {distances}")
    if node == "E":
        dijkstra_path = distances

shortest_path_edges = list(
    zip(
        nx.shortest_path(graph, source="A", target="E", weight="weight"),
        nx.shortest_path(graph, source="A", target="E", weight="weight")[1:],
    )
)
visualize_graph(
    graph, highlight_edges=shortest_path_edges, title="Dijkstra's Shortest Path"
)

# Run and Visualize A* Algorithm
a_star_path = a_star(graph_dict, start="A", goal="E", heuristic=heuristic)
print("A* Shortest Path:", a_star_path)
a_star_edges = list(zip(a_star_path, a_star_path[1:]))
visualize_graph(graph, highlight_edges=a_star_edges, title="A* Shortest Path")

# Run and Visualize Bellman-Ford Algorithm
bellman_ford_result = bellman_ford(graph_dict, source="A")
print("Bellman-Ford Shortest Distances:", bellman_ford_result)

# Run and Visualize Prim's Algorithm
prim_result = prim(graph_dict, start="A")
print("Prim's MST:", prim_result)
prim_edges = [(u, v) for u, v, _ in prim_result]
visualize_graph(graph, highlight_edges=prim_edges, title="Prim's Minimum Spanning Tree")
