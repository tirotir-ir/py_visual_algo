from py_visual_algo.algorithms.graph import dfs

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
result = dfs(graph, "A")
print("DFS Traversal Order:", result)
