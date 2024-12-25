from py_visual_algo.algorithms.evolutionary.harmony_search import harmony_search
import random


# Define fitness function
def fitness_fn(harmony):
    return -sum((x - 5) ** 2 for x in harmony)


# Define solution generator
def generate_fn():
    return [random.uniform(-10, 10) for _ in range(5)]


# Example usage
best_harmony = harmony_search(
    fitness_fn, generate_fn, memory_size=10, max_iterations=100, hmcr=0.9, par=0.3
)
print("Best Harmony:", best_harmony)
