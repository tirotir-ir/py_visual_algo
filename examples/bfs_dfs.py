import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


def bfs_with_edges(graph, start):
    """
    Perform BFS and track edges traversed.

    Args:
        graph (dict): Graph represented as adjacency list.
        start: Starting node.

    Returns:
        list: Nodes visited in BFS order.
        list: Edges traversed during BFS.
    """
    visited = []
    edges = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    edges.append((node, neighbor))
                    queue.append(neighbor)

    return visited, edges


def dfs_with_edges(graph, start, visited=None, edges=None):
    """
    Perform DFS and track edges traversed.

    Args:
        graph (dict): Graph represented as adjacency list.
        start: Starting node.
        visited (set): Set of visited nodes.
        edges (list): List of edges traversed during DFS.

    Returns:
        list: Nodes visited in DFS order.
        list: Edges traversed during DFS.
    """
    if visited is None:
        visited = set()
    if edges is None:
        edges = []

    visited.add(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            edges.append((start, neighbor))
            dfs_with_edges(graph, neighbor, visited, edges)

    return list(visited), edges


def visualize_graph_with_edges(graph, traversed_edges, title="Graph Traversal"):
    """
    Visualize a graph with highlighted traversed edges.

    Args:
        graph (nx.Graph): NetworkX graph object.
        traversed_edges (list): List of edges to highlight.
        title (str): Title of the graph plot.
    """
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color="lightblue", font_weight="bold")
    nx.draw_networkx_edges(
        graph, pos, edgelist=traversed_edges, edge_color="red", width=2
    )
    plt.title(title)
    plt.show()


# Define the graph as adjacency list
graph_dict = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"],
}

# Convert adjacency list to NetworkX graph
graph = nx.Graph()
for node, neighbors in graph_dict.items():
    for neighbor in neighbors:
        graph.add_edge(node, neighbor)

# Run BFS and visualize
bfs_nodes, bfs_edges = bfs_with_edges(graph_dict, start="A")
print("BFS Order:", bfs_nodes)
visualize_graph_with_edges(graph, bfs_edges, title="BFS Traversal")

# Run DFS and visualize
dfs_nodes, dfs_edges = dfs_with_edges(graph_dict, start="A")
print("DFS Order:", dfs_nodes)
visualize_graph_with_edges(graph, dfs_edges, title="DFS Traversal")
