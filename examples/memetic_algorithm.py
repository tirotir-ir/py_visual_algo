from py_visual_algo.algorithms.evolutionary.memetic_algorithm import memetic_algorithm
import random


# Define fitness function
def fitness_fn(individual):
    return sum(individual)


# Define mutation function
def mutate_fn(individual):
    index = random.randint(0, len(individual) - 1)
    individual[index] += random.uniform(-1, 1)
    return individual


# Define crossover function
def crossover_fn(parent1, parent2):
    midpoint = len(parent1) // 2
    return parent1[:midpoint] + parent2[midpoint:]


# Define local search function
def local_search_fn(individual):
    return [x + random.uniform(-0.1, 0.1) for x in individual]


# Example usage
if __name__ == "__main__":
    population = [[random.uniform(-10, 10) for _ in range(5)] for _ in range(20)]
    best_solution = memetic_algorithm(
        population,
        fitness_fn,
        mutate_fn,
        crossover_fn,
        local_search_fn,
        max_generations=50,
    )
    print("Best Solution:", best_solution)
