from py_visual_algo.algorithms.evolutionary.artificial_bee_colony import (
    artificial_bee_colony,
)
import random


# Define fitness function
def fitness_fn(solution):
    return sum(solution)


# Define solution generator
def generate_fn():
    return [random.uniform(-10, 10) for _ in range(5)]


# Example usage
best_solution = artificial_bee_colony(
    fitness_fn, generate_fn, population_size=20, max_iterations=100
)
print("Best Solution Found:", best_solution)
