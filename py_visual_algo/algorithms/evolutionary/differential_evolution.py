import random


def differential_evolution(
    population,
    fitness_fn,
    mutation_factor=0.8,
    crossover_probability=0.9,
    max_generations=100,
):
    """
    Differential Evolution (DE) implementation.

    Args:
        population (list): Initial population.
        fitness_fn (function): Fitness evaluation function.
        mutation_factor (float): Mutation scaling factor.
        crossover_probability (float): Probability of crossover.
        max_generations (int): Maximum number of generations.

    Returns:
        Best individual found.
    """
    for generation in range(max_generations):
        new_population = []
        for i in range(len(population)):
            a, b, c = random.sample([x for j, x in enumerate(population) if j != i], 3)
            mutant = [a[k] + mutation_factor * (b[k] - c[k]) for k in range(len(a))]

            trial = [
                (
                    mutant[k]
                    if random.random() < crossover_probability
                    else population[i][k]
                )
                for k in range(len(mutant))
            ]

            if fitness_fn(trial) > fitness_fn(population[i]):
                new_population.append(trial)
            else:
                new_population.append(population[i])

        population = new_population

    return max(population, key=fitness_fn)
