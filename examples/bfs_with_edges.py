from py_visual_algo.algorithms.graph import bfs_with_edges

graph = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}
nodes, edges = bfs_with_edges(graph, "A")
print("BFS Traversal Order:", nodes)
print("BFS Traversed Edges:", edges)
