import random


def artificial_bee_colony(
    fitness_fn, generate_fn, population_size=20, max_iterations=100
):
    """
    Artificial Bee Colony (ABC) implementation.

    Args:
        fitness_fn (function): Fitness evaluation function.
        generate_fn (function): Function to generate new solutions.
        population_size (int): Number of bees in the population.
        max_iterations (int): Maximum number of iterations.

    Returns:
        Best solution found.
    """
    # Initialize population
    population = [generate_fn() for _ in range(population_size)]
    fitness = [fitness_fn(ind) for ind in population]
    trial_counts = [0] * population_size

    for _ in range(max_iterations):
        # Employed bees phase
        for i in range(population_size):
            new_solution = generate_fn()
            new_fitness = fitness_fn(new_solution)
            if new_fitness > fitness[i]:
                population[i] = new_solution
                fitness[i] = new_fitness
                trial_counts[i] = 0
            else:
                trial_counts[i] += 1

        # Onlooker bees phase
        total_fitness = sum(fitness)
        probabilities = [f / total_fitness for f in fitness]
        for i in range(population_size):
            if random.random() < probabilities[i]:
                new_solution = generate_fn()
                new_fitness = fitness_fn(new_solution)
                if new_fitness > fitness[i]:
                    population[i] = new_solution
                    fitness[i] = new_fitness

        # Scout bees phase
        for i in range(population_size):
            if trial_counts[i] > 10:  # Hardcoded scout limit
                population[i] = generate_fn()
                fitness[i] = fitness_fn(population[i])
                trial_counts[i] = 0

    # Return the best solution found
    best_index = fitness.index(max(fitness))
    return population[best_index]
