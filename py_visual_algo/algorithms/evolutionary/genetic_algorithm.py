import random


def genetic_algorithm(
    population,
    fitness_fn,
    mutate_fn,
    crossover_fn,
    max_generations=100,
    mutation_rate=0.1,
):
    """
    Genetic Algorithm implementation.

    Args:
        population (list): Initial population.
        fitness_fn (function): Function to evaluate fitness.
        mutate_fn (function): Function to mutate individuals.
        crossover_fn (function): Function to perform crossover.
        max_generations (int): Maximum number of generations.
        mutation_rate (float): Probability of mutation.

    Yields:
        tuple: (generation, population)
    """
    for generation in range(max_generations):
        population = sorted(population, key=fitness_fn, reverse=True)
        yield generation, population

        # Selection
        top_half = population[: len(population) // 2]

        # Crossover
        offspring = []
        for _ in range(len(population) - len(top_half)):
            parent1, parent2 = random.sample(top_half, 2)
            child = crossover_fn(parent1, parent2)
            offspring.append(child)

        # Mutation
        population = top_half + [
            mutate_fn(ind) if random.random() < mutation_rate else ind
            for ind in offspring
        ]
