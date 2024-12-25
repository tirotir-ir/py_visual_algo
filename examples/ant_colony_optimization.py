from py_visual_algo.algorithms.evolutionary.ant_colony import ant_colony_optimization

# Define graph as adjacency list with weights
graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3, "A": 6},  # Add edge from E to A to form a complete cycle
}

# Run Ant Colony Optimization
best_path = ant_colony_optimization(
    graph,
    ants=10,
    iterations=50,
    alpha=1.0,
    beta=2.0,
    evaporation=0.5,
    initial_pheromone=1.0,
)

print("Best Path Found:", best_path)
