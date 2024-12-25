from py_visual_algo.algorithms.graph import bfs

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
result = bfs(graph, "A")
print("BFS Traversal Order:", result)
