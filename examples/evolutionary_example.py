from py_visual_algo.algorithms.evolutionary import genetic_algorithm
import random


def fitness_fn(individual):
    """Fitness is the sum of the individual's values."""
    return sum(individual)


def mutate_fn(individual):
    """Randomly mutate one element of the individual."""
    index = random.randint(0, len(individual) - 1)
    individual[index] = random.randint(0, 100)
    return individual


def crossover_fn(parent1, parent2):
    """Simple one-point crossover."""
    point = len(parent1) // 2
    return parent1[:point] + parent2[point:]


if __name__ == "__main__":
    # Create an initial population
    population = [[random.randint(0, 100) for _ in range(5)] for _ in range(10)]
    generator = genetic_algorithm(
        population,
        fitness_fn,
        mutate_fn,
        crossover_fn,
        max_generations=10,
        mutation_rate=0.2,
    )

    for generation, pop in generator:
        best_individual = max(pop, key=fitness_fn)
        print(f"Generation {generation}: Best Fitness = {fitness_fn(best_individual)}")
