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
    Basic Genetic Algorithm.

    Args:
        population (list): Initial population.
        fitness_fn (function): Function to evaluate the fitness of an individual.
        mutate_fn (function): Function to mutate an individual.
        crossover_fn (function): Function to perform crossover between two parents.
        max_generations (int): Maximum number of generations to simulate.
        mutation_rate (float): Probability of mutating an individual.

    Yields:
        tuple: Current generation number and the population.
    """
    for generation in range(max_generations):
        # Sort population by fitness (higher is better)
        population = sorted(population, key=fitness_fn, reverse=True)
        yield generation, population

        # Selection: Take the top 50% of the population
        top_half = population[: len(population) // 2]

        # Crossover to generate offspring
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
