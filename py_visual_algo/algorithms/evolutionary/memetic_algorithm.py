import random


def memetic_algorithm(
    population,
    fitness_fn,
    mutate_fn,
    crossover_fn,
    local_search_fn,
    max_generations=100,
):
    """
    Memetic Algorithm implementation.

    Args:
        population (list): List of individuals in the population.
        fitness_fn (function): Function to evaluate the fitness of an individual.
        mutate_fn (function): Function to mutate an individual.
        crossover_fn (function): Function to perform crossover between two parents.
        local_search_fn (function): Function to perform local search on an individual.
        max_generations (int): Maximum number of generations to run the algorithm.

    Returns:
        list: The best solution found by the algorithm.
    """
    for generation in range(max_generations):
        # Evaluate fitness of the population
        population = sorted(population, key=fitness_fn, reverse=True)

        # Selection: Take the top 50% of the population
        top_half = population[: len(population) // 2]

        # Crossover to create offspring
        offspring = [
            crossover_fn(random.choice(top_half), random.choice(top_half))
            for _ in range(len(population) - len(top_half))
        ]

        # Mutation
        offspring = [
            mutate_fn(ind) if random.random() < 0.1 else ind for ind in offspring
        ]

        # Local Search
        offspring = [local_search_fn(ind) for ind in offspring]

        # Create the next generation
        population = top_half + offspring

    # Return the best solution
    return max(population, key=fitness_fn)
