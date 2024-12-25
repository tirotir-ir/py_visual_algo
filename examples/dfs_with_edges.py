from py_visual_algo.algorithms.graph import dfs_with_edges

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
nodes, edges = dfs_with_edges(graph, "A")
print("DFS Traversal Order:", nodes)
print("DFS Traversed Edges:", edges)
