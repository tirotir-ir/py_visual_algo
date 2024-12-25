import random
from py_visual_algo.algorithms.evolutionary.particle_swarm import (
    particle_swarm_optimization,
)


# Define fitness function
def fitness_fn(particle):
    """
    Fitness function to evaluate the quality of a particle.

    Args:
        particle (list): A list representing the particle's position.

    Returns:
        float: The fitness value of the particle.
    """
    return -sum((x - 5) ** 2 for x in particle)


if __name__ == "__main__":
    # Initialize a random population of particles (20 particles in 5D space)
    population = [[random.uniform(-10, 10) for _ in range(5)] for _ in range(20)]

    # Run the particle swarm optimization algorithm
    best_particle = particle_swarm_optimization(
        population=population,
        fitness_fn=fitness_fn,
        inertia=0.5,  # Inertia coefficient
        cognitive=1.5,  # Cognitive coefficient
        social=2.0,  # Social coefficient
        max_iterations=100,  # Maximum number of iterations
    )

    print("\nBest Particle Found:", best_particle)
    print("Best Particle Fitness:", fitness_fn(best_particle))
