def ant_colony_optimization(
    graph, ants, iterations, alpha, beta, evaporation, initial_pheromone
):
    """
    Ant Colony Optimization implementation.

    Args:
        graph (dict): Adjacency list representation of the graph with edge weights.
        ants (int): Number of ants in the colony.
        iterations (int): Number of iterations.
        alpha (float): Influence of pheromone levels.
        beta (float): Influence of edge weights.
        evaporation (float): Pheromone evaporation rate.
        initial_pheromone (float): Initial pheromone level for all edges.

    Returns:
        list: The best path found by the algorithm.
    """
    # Initialize pheromone levels for all edges
    pheromone = {
        (node, neighbor): initial_pheromone
        for node, neighbors in graph.items()
        for neighbor in neighbors
    }

    best_path = None
    best_path_cost = float("inf")

    for _ in range(iterations):
        all_paths = []
        all_costs = []

        # Each ant generates a path
        for _ in range(ants):
            path = []
            visited = set()
            current = next(iter(graph))  # Start from any node (e.g., the first one)
            path_cost = 0

            while len(visited) < len(graph):
                visited.add(current)
                path.append(current)

                # Select the next node
                neighbors = [n for n in graph[current] if n not in visited]
                if not neighbors:
                    break

                next_node = max(
                    neighbors,
                    key=lambda x: (pheromone[(current, x)] ** alpha)
                    * (1 / graph[current][x] ** beta),
                )

                path_cost += graph[current][next_node]
                current = next_node

            # Complete the cycle (if applicable)
            if len(path) == len(graph) and path[0] in graph[current]:
                path_cost += graph[current][path[0]]
                path.append(path[0])

            all_paths.append(path)
            all_costs.append(path_cost)

        # Update the best path
        min_cost = min(all_costs)
        if min_cost < best_path_cost:
            best_path_cost = min_cost
            best_path = all_paths[all_costs.index(min_cost)]

        # Pheromone evaporation
        for edge in pheromone:
            pheromone[edge] *= 1 - evaporation

        # Pheromone deposit
        for path, cost in zip(all_paths, all_costs):
            for i in range(len(path) - 1):
                pheromone[(path[i], path[i + 1])] += 1 / cost

    return best_path
