import math
import random


def simulated_annealing(
    initial_state, fitness_fn, neighbor_fn, temp_fn, max_iterations=1000
):
    """
    Simulated Annealing implementation.

    Args:
        initial_state: The initial solution state.
        fitness_fn (function): Fitness evaluation function.
        neighbor_fn (function): Neighbor state generator.
        temp_fn (function): Temperature function.
        max_iterations (int): Maximum iterations.

    Returns:
        Best solution found.
    """
    current_state = initial_state
    best_state = initial_state

    for t in range(1, max_iterations + 1):
        temperature = temp_fn(t)
        if temperature <= 0:
            break

        neighbor = neighbor_fn(current_state)
        delta = fitness_fn(neighbor) - fitness_fn(current_state)

        if delta > 0 or random.random() < math.exp(delta / temperature):
            current_state = neighbor

        if fitness_fn(current_state) > fitness_fn(best_state):
            best_state = current_state

    return best_state
