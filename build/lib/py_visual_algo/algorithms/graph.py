import heapq
from collections import deque


def bfs(graph, start):
    """
    Breadth-First Search (BFS) implementation.

    Args:
        graph (dict): Graph represented as an adjacency list.
        start: Starting node.

    Returns:
        list: Nodes visited in BFS order.
    """
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(
                neighbor for neighbor in graph[node] if neighbor not in visited
            )

    return visited


def bfs_with_edges(graph, start):
    """
    Breadth-First Search (BFS) with edge tracking.

    Args:
        graph (dict): Graph represented as an adjacency list.
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
    Depth-First Search (DFS) with edge tracking.

    Args:
        graph (dict): Graph represented as an adjacency list.
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


def dfs(graph, start, visited=None):
    """
    Depth-First Search (DFS) implementation.

    Args:
        graph (dict): Graph represented as an adjacency list.
        start: Starting node.
        visited (set): Set of visited nodes.

    Returns:
        list: Nodes visited in DFS order.
    """
    if visited is None:
        visited = set()

    visited.add(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return list(visited)


def dijkstra(graph, start):
    """
    Dijkstra's Algorithm implementation.

    Args:
        graph (dict): Graph represented as an adjacency dictionary.
        start: Starting node.

    Yields:
        tuple: Current node and distances.
    """
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        yield current_node, distances

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))


def a_star(graph, start, goal, heuristic):
    """
    A* Algorithm implementation.

    Args:
        graph (dict): Graph represented as an adjacency dictionary.
        start: Starting node.
        goal: Goal node.
        heuristic (dict): Heuristic values for nodes.

    Returns:
        list: Shortest path from start to goal.
    """
    open_set = [(0, start)]
    came_from = {}
    g_score = {node: float("inf") for node in graph}
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]  # Reverse path

        for neighbor, weight in graph[current].items():
            tentative_g_score = g_score[current] + weight
            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic.get(
                    neighbor, float("inf")
                )
                heapq.heappush(open_set, (f_score[neighbor], neighbor))

    raise ValueError(f"No path found from {start} to {goal}")


def bellman_ford(graph, source):
    """
    Bellman-Ford Algorithm for single-source shortest paths.

    Args:
        graph (list): List of edges (u, v, weight).
        source: Source node.

    Returns:
        dict: Shortest distances from the source to each node.
    """
    distance = {node: float("inf") for node in graph}
    distance[source] = 0

    for _ in range(len(graph) - 1):
        for u, neighbors in graph.items():
            for v, weight in neighbors.items():
                if distance[u] + weight < distance[v]:
                    distance[v] = distance[u] + weight

    for u, neighbors in graph.items():
        for v, weight in neighbors.items():
            if distance[u] + weight < distance[v]:
                raise ValueError("Graph contains a negative-weight cycle")

    return distance


def prim(graph, start):
    """
    Prim's Algorithm for Minimum Spanning Tree (MST).

    Args:
        graph (dict): Graph represented as an adjacency dictionary.
        start: Starting node.

    Returns:
        list: Edges in the MST.
    """
    mst = []
    visited = set()
    edges = [(weight, start, neighbor) for neighbor, weight in graph[start].items()]
    heapq.heapify(edges)

    while edges:
        weight, u, v = heapq.heappop(edges)
        if v not in visited:
            visited.add(v)
            mst.append((u, v, weight))

            for neighbor, w in graph[v].items():
                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst
