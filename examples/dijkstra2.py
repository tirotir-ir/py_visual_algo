import networkx as nx
from py_visual_algo.algorithms.pathfinding import dijkstra

# Convert the dictionary to a networkx graph
graph_dict = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1},
}
graph = nx.Graph()
for node, neighbors in graph_dict.items():
    for neighbor, weight in neighbors.items():
        graph.add_edge(node, neighbor, weight=weight)

# Starting node for Dijkstra's algorithm
start_node = "A"

# Run Dijkstra's algorithm
generator = dijkstra(graph, start_node)

# Print the step-by-step output
print("Dijkstra's Algorithm:")
for current_node, distances in generator:
    print(f"Current Node: {current_node}, Distances: {distances}")
