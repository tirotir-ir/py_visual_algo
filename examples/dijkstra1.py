from py_visual_algo.algorithms.graph import dijkstra

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3},
}
generator = dijkstra(graph, "A")
for node, distances in generator:
    print(f"Node: {node}, Distances: {distances}")
