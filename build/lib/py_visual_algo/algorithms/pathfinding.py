from heapq import heappop, heappush


def dijkstra(graph, start):
    """Dijkstra's algorithm using networkx for graph representation."""
    distances = {node: float("inf") for node in graph.nodes}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        yield current_node, distances

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor].get("weight", 1)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heappush(priority_queue, (distance, neighbor))


def a_star(graph, start, goal, heuristic):
    """
    A* Algorithm using networkx for graph representation.

    Args:
        graph (nx.Graph): The graph to search.
        start (str): The starting node.
        goal (str): The target node.
        heuristic (dict): Heuristic values for nodes.

    Yields:
        tuple: Current node and f-scores dictionary.
    """
    open_set = [(0, start)]
    g_score = {node: float("inf") for node in graph.nodes}
    g_score[start] = 0
    f_score = {node: float("inf") for node in graph.nodes}
    f_score[start] = heuristic[start]

    while open_set:
        _, current = heappop(open_set)

        if current == goal:
            yield current, f_score  # Yield final state
            return

        yield current, f_score  # Yield current node and f-scores

        for neighbor in graph.neighbors(current):
            tentative_g_score = g_score[current] + graph[current][neighbor].get(
                "weight", 1
            )
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic.get(
                    neighbor, float("inf")
                )
                heappush(open_set, (f_score[neighbor], neighbor))
