from py_visual_algo.algorithms.graph import bellman_ford

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3},
}
result = bellman_ford(graph, "A")
print("Bellman-Ford Shortest Distances:", result)
