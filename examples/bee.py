from py_visual_algo.algorithms.evolutionary.artificial_bee_colony import (
    artificial_bee_colony,
)
import random


# Define the fitness function
def fitness_fn(solution):
    """
    Fitness function: Maximize the sum of squares of the elements in the solution.

    Args:
        solution (list): A list of numbers.

    Returns:
        float: The fitness value of the solution.
    """
    return sum(x**2 for x in solution)


# Define the solution generator
def generate_fn():
    """
    Generate a random solution.

    Returns:
        list: A solution represented as a list of random numbers.
    """
    return [random.uniform(-10, 10) for _ in range(5)]  # 5-dimensional solution space


# Run the Artificial Bee Colony (ABC) algorithm
if __name__ == "__main__":
    best_solution = artificial_bee_colony(
        fitness_fn=fitness_fn,
        generate_fn=generate_fn,
        population_size=20,  # Number of bees
        max_iterations=100,  # Maximum iterations
    )

    print("Best solution found:", best_solution)
    print("Best solution fitness:", fitness_fn(best_solution))
