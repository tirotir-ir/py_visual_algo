from py_visual_algo.algorithms.evolutionary.simulated_annealing import (
    simulated_annealing,
)
import random


# Define fitness function
def fitness_fn(state):
    return -sum((x - 3) ** 2 for x in state)


# Define neighbor function
def neighbor_fn(state):
    index = random.randint(0, len(state) - 1)
    new_state = state[:]
    new_state[index] += random.uniform(-0.5, 0.5)
    return new_state


# Define temperature function
def temp_fn(t):
    return max(1.0, 100 / (t + 1))


# Example usage
initial_state = [random.uniform(-10, 10) for _ in range(5)]
best_state = simulated_annealing(
    initial_state, fitness_fn, neighbor_fn, temp_fn, max_iterations=1000
)
print("Best State:", best_state)
