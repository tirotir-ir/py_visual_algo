### **`usage.md`**
```markdown
# Usage Guide

This guide provides instructions and examples to help you use the `py_visual_algo` library effectively.

## Importing the Library
Start by importing the required modules:
```python
from py_visual_algo.algorithms.sorting import bubble_sort
from py_visual_algo.visualizer.plotter import plot_sorting
```
### Examples
## Sorting Example
```python
from py_visual_algo.algorithms.sorting import bubble_sort

data = [5, 3, 8, 6, 2]
print("Original Data:", data)

for step in bubble_sort(data):
    print("Sorting Step:", step)

print("Sorted Data:", data)
```
## Graph Visualization Example
```python
from py_visual_algo.algorithms.graph import dijkstra
from py_visual_algo.visualizer.plot_graph import plot_graph

graph = {
    "A": {"B": 1, "C": 4},
    "B": {"A": 1, "C": 2, "D": 5},
    "C": {"A": 4, "B": 2, "D": 1},
    "D": {"B": 5, "C": 1, "E": 3},
    "E": {"D": 3},
}

shortest_path = dijkstra(graph, start="A")
plot_graph(graph, path=shortest_path)
```
## Optimization Example
```python
from py_visual_algo.algorithms.evolutionary.particle_swarm import particle_swarm_optimization
import random

def fitness_fn(particle):
    return -sum((x - 5) ** 2 for x in particle)

population = [[random.uniform(-10, 10) for _ in range(5)] for _ in range(20)]
best_particle = particle_swarm_optimization(population, fitness_fn)
print("Best Particle:", best_particle)
```
For more examples, refer to the examples directory.