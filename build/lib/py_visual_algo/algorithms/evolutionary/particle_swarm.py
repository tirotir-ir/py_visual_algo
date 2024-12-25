import random


def particle_swarm_optimization(
    population,
    fitness_fn,
    inertia=0.5,
    cognitive=1.5,
    social=2.0,
    max_iterations=100,
):
    """
    Simplified Particle Swarm Optimization implementation.

    Args:
        population (list): List of particles, where each particle is a list of position values.
        fitness_fn (function): Function to evaluate the fitness of a particle.
        inertia (float): Inertia coefficient for velocity update.
        cognitive (float): Cognitive coefficient for personal best influence.
        social (float): Social coefficient for global best influence.
        max_iterations (int): Maximum number of iterations to perform.

    Returns:
        list: The best particle found by the algorithm.
    """
    # Initialize velocities, personal best, and global best
    dimensions = len(population[0])
    velocities = [
        [random.uniform(-1, 1) for _ in range(dimensions)] for _ in population
    ]
    personal_best = population[:]
    personal_best_scores = [fitness_fn(p) for p in personal_best]
    global_best = personal_best[personal_best_scores.index(max(personal_best_scores))]

    for iteration in range(max_iterations):
        for i, particle in enumerate(population):
            # Update velocity
            velocities[i] = [
                inertia * velocities[i][d]
                + cognitive * random.random() * (personal_best[i][d] - particle[d])
                + social * random.random() * (global_best[d] - particle[d])
                for d in range(dimensions)
            ]

            # Update particle position
            population[i] = [particle[d] + velocities[i][d] for d in range(dimensions)]

            # Update personal best
            fitness = fitness_fn(population[i])
            if fitness > personal_best_scores[i]:
                personal_best[i] = population[i][:]
                personal_best_scores[i] = fitness

        # Update global best
        best_index = personal_best_scores.index(max(personal_best_scores))
        global_best = personal_best[best_index]

        # Debugging: Print progress
        print(
            f"Iteration {iteration + 1}/{max_iterations}, Best Fitness: {max(personal_best_scores)}"
        )

    return global_best
