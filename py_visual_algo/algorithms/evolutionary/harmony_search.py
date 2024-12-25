import random


def harmony_search(
    fitness_fn, generate_fn, memory_size=10, max_iterations=100, hmcr=0.9, par=0.3
):
    """
    Harmony Search (HS) implementation.

    Args:
        fitness_fn (function): Fitness evaluation function.
        generate_fn (function): Function to generate new solutions.
        memory_size (int): Size of the harmony memory.
        max_iterations (int): Maximum number of iterations.
        hmcr (float): Harmony Memory Consideration Rate.
        par (float): Pitch Adjustment Rate.

    Returns:
        Best solution found.
    """
    # Initialize harmony memory
    harmony_memory = [generate_fn() for _ in range(memory_size)]
    fitness = [fitness_fn(harmony) for harmony in harmony_memory]

    for _ in range(max_iterations):
        new_harmony = []
        for i in range(len(harmony_memory[0])):
            if random.random() < hmcr:  # Consider Harmony Memory
                harmony = random.choice(harmony_memory)
                new_harmony.append(harmony[i])
                if random.random() < par:  # Pitch adjustment
                    new_harmony[-1] += random.uniform(-0.01, 0.01)  # Small adjustment
            else:
                new_harmony.append(random.uniform(-1, 1))  # Random value

        new_fitness = fitness_fn(new_harmony)
        # Replace the worst harmony if the new one is better
        worst_index = fitness.index(min(fitness))
        if new_fitness > fitness[worst_index]:
            harmony_memory[worst_index] = new_harmony
            fitness[worst_index] = new_fitness

    # Return the best solution
    best_index = fitness.index(max(fitness))
    return harmony_memory[best_index]
