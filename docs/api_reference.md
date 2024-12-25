# API Reference

This document provides a detailed reference of all the modules, classes, and functions in the `py_visual_algo` library.

## Modules

### `py_visual_algo.algorithms`
- **`sorting`**
  - `bubble_sort(data)` - Performs Bubble Sort on the input data.
  - `merge_sort(data)` - Performs Merge Sort on the input data.
  - `quick_sort(data)` - Performs Quick Sort on the input data.
- **`searching`**
  - `linear_search(data, target)` - Finds the target using Linear Search.
  - `binary_search(data, target)` - Finds the target using Binary Search.
  - `jump_search(data, target)` - Finds the target using Jump Search.
- **`graph`**
  - `bfs(graph, start)` - Breadth-First Search traversal.
  - `dfs(graph, start)` - Depth-First Search traversal.
  - `dijkstra(graph, start)` - Finds the shortest path using Dijkstra's algorithm.
  - `a_star(graph, start, goal, heuristic)` - Finds the shortest path using A* algorithm.
  - `bellman_ford(graph, start)` - Finds the shortest path using Bellman-Ford algorithm.
  - `prim(graph, start)` - Finds the minimum spanning tree using Prim's algorithm.
- **`trees`**
  - `inorder_traversal(root)` - Performs Inorder Traversal of a tree.
  - `preorder_traversal(root)` - Performs Preorder Traversal of a tree.
  - `postorder_traversal(root)` - Performs Postorder Traversal of a tree.
- **`evolutionary`**
  - `genetic_algorithm(...)` - Implements the Genetic Algorithm.
  - `simulated_annealing(...)` - Implements Simulated Annealing.
  - `particle_swarm_optimization(...)` - Implements Particle Swarm Optimization.
  - `differential_evolution(...)` - Implements Differential Evolution.
  - `ant_colony_optimization(...)` - Implements Ant Colony Optimization.
  - `memetic_algorithm(...)` - Implements the Memetic Algorithm.
  - `artificial_bee_colony(...)` - Implements Artificial Bee Colony Optimization.
  - `harmony_search(...)` - Implements Harmony Search.
  - `cultural_algorithm(...)` - Implements Cultural Algorithm.

### `py_visual_algo.visualizer`
- `plot_sorting(data_gen, title="Sorting Visualization", speed=0.5)` - Visualizes sorting steps.
- `plot_graph(graph, path=None)` - Visualizes a graph and its path.

### `py_visual_algo.ui`
- `cli()` - Command-line interface for `py_visual_algo`.
- `launch_gui()` - Graphical user interface for `py_visual_algo`.

Refer to the respective modules for detailed docstrings and examples.
