from py_visual_algo.algorithms.graph import a_star

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3},
}
heuristic = {"A": 7, "B": 6, "C": 2, "D": 1, "E": 0}
path = a_star(graph, "A", "E", heuristic)
print("A* Shortest Path:", path)
