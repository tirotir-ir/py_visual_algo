from py_visual_algo.algorithms.evolutionary.differential_evolution import (
    differential_evolution,
)
import random


# Define fitness function
def fitness_fn(individual):
    return -sum((x - 5) ** 2 for x in individual)


# Example usage
population = [[random.uniform(-10, 10) for _ in range(5)] for _ in range(20)]
best_individual = differential_evolution(
    population,
    fitness_fn,
    mutation_factor=0.8,
    crossover_probability=0.9,
    max_generations=100,
)
print("Best Individual:", best_individual)
