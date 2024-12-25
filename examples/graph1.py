from py_visual_algo.algorithms.graph import bfs
from py_visual_algo.algorithms.graph import dfs
from py_visual_algo.algorithms.graph import dijkstra
from py_visual_algo.algorithms.graph import a_star
from py_visual_algo.algorithms.graph import bellman_ford
from py_visual_algo.algorithms.graph import prim

# Sample graph
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3},
}

# Heuristic for A*
heuristic = {
    "A": 7,
    "B": 6,
    "C": 2,
    "D": 1,
    "E": 0,
}

# Run BFS
print("BFS:", bfs(graph, start="A"))

# Run DFS
print("DFS:", dfs(graph, start="A"))

# Run Dijkstra's
for node, distances in dijkstra(graph, start="A"):
    print(f"Dijkstra's - Node: {node}, Distances: {distances}")

# Run A*
print("A*:", a_star(graph, start="A", goal="E", heuristic=heuristic))

# Run Bellman-Ford
print("Bellman-Ford:", bellman_ford(graph, source="A"))

# Run Prim's
print("Prim's MST:", prim(graph, start="A"))
