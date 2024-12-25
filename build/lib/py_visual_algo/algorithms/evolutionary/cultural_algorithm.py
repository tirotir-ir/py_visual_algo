import random


def cultural_algorithm(
    population, fitness_fn, mutate_fn, crossover_fn, belief_space, max_generations=100
):
    """
    Cultural Algorithm (CA) implementation.

    Args:
        population (list): Initial population.
        fitness_fn (function): Fitness evaluation function.
        mutate_fn (function): Mutation function.
        crossover_fn (function): Crossover function.
        belief_space (dict): A dictionary to store beliefs and ranges.
        max_generations (int): Maximum number of generations.

    Returns:
        Best solution found.
    """
    for generation in range(max_generations):
        # Evaluate fitness
        population = sorted(population, key=fitness_fn, reverse=True)

        # Update belief space
        best_individual = population[0]
        for key in belief_space:
            belief_space[key] = update_belief(belief_space[key], best_individual)

        # Generate new population
        new_population = []
        for _ in range(len(population)):
            if random.random() < 0.5:
                # Use mutation
                individual = mutate_fn(random.choice(population))
            else:
                # Use crossover
                parent1, parent2 = random.sample(population, 2)
                individual = crossover_fn(parent1, parent2)
            new_population.append(individual)

        population = new_population

    return max(population, key=fitness_fn)


def update_belief(belief_range, individual):
    """
    Update belief space with new information.

    Args:
        belief_range (tuple): Current belief range (min, max).
        individual (list): Individual from the population.

    Returns:
        tuple: Updated belief range.
    """
    min_val, max_val = belief_range
    new_min = min(min_val, min(individual))
    new_max = max(max_val, max(individual))
    return new_min, new_max
