import networkx as nx
from py_visual_algo.algorithms.pathfinding import dijkstra, a_star

# Create a graph
graph = nx.Graph()
graph.add_weighted_edges_from(
    [
        ("A", "B", 1),
        ("A", "C", 4),
        ("B", "C", 2),
        ("B", "D", 5),
        ("C", "D", 1),
        ("D", "E", 3),
    ]
)

# Define heuristic for A*
heuristic = {"A": 7, "B": 6, "C": 2, "D": 1, "E": 0}

# Run Dijkstra's algorithm
print("Dijkstra's Algorithm:")
for node, distances in dijkstra(graph, "A"):
    print(f"Current node: {node}, Distances: {distances}")

# Run A* algorithm
print("\nA* Algorithm:")
for node, f_scores in a_star(graph, "A", "E", heuristic):
    print(f"Current node: {node}, f-scores: {f_scores}")
