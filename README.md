# **py_visual_algo**
Interactive Algorithm Visualizer for Python

# Overview

`py_visual_algo` is a Python library designed for visualizing and understanding algorithms, including sorting, searching, graph traversal, and evolutionary algorithms. Using real-time visualizations and step-by-step animations, it transforms complex algorithmic concepts into intuitive, interactive experiences. Perfect for educators, students, and developers, `py_visual_algo` bridges the gap between theoretical concepts and practical implementation.

## Features

- **Real-Time Visualizations**  
  Watch algorithms execute in real-time with live updates and insights.

- **Step-by-Step Animations**  
  Follow every decision, iteration, and operation of an algorithm.

- **Graph Integration**  
  Leverage `networkx` to visualize and work with graph-based algorithms.

- **Evolutionary Algorithms**  
  Explore optimization problems with cutting-edge techniques like genetic algorithms, particle swarm optimization, and more.

- **Extensive Algorithm Coverage**  
  Includes a wide range of algorithms such as:
  - Sorting: Bubble Sort, Quick Sort, Merge Sort.
  - Searching: Linear Search, Binary Search, Jump Search.
  - Graph Algorithms: BFS, DFS, Dijkstra, A*.
  - Evolutionary Algorithms: Genetic Algorithm, Particle Swarm Optimization, Ant Colony Optimization.

- **Customizable API**  
  Tailor algorithm visualizations, themes, and execution parameters to fit your unique requirements.

- **Educational Focus**  
  Designed for teaching, learning, and presentations, making it the ideal tool for instructors and students.

Whether you're an educator aiming to simplify algorithmic concepts, a student trying to grasp algorithms interactively, or a developer experimenting with optimization techniques, `py_visual_algo` is your go-to solution.


# Algorithms Included in `py_visual_algo`

## Sorting Algorithms
- `bubble_sort(data)` - Bubble Sort
- `merge_sort(data)` - Merge Sort
- `quick_sort(data)` - Quick Sort
- `insertion_sort(data)` - Insertion Sort
- `selection_sort(data)` - Selection Sort
- `heap_sort(data)` - Heap Sort
- `radix_sort(data)` - Radix Sort
- `counting_sort(data)` - Counting Sort
- `bucket_sort(data)` - Bucket Sort
- `shell_sort(data)` - Shell Sort

---

## Searching Algorithms
- `linear_search(data, target)` - Linear Search
- `binary_search(data, target)` - Binary Search
- `jump_search(data, target)` - Jump Search
- `exponential_search(data, target)` - Exponential Search
- `interpolation_search(data, target)` - Interpolation Search

---

## Graph Algorithms
- `bfs(graph, start)` - Breadth-First Search (BFS)
- `dfs(graph, start)` - Depth-First Search (DFS)
- `bfs_with_edges(graph, start)` - BFS with Edge Visualization
- `dfs_with_edges(graph, start)` - DFS with Edge Visualization
- `dijkstra(graph, start)` - Dijkstra's Algorithm
- `a_star(graph, start, goal, heuristic)` - A* Algorithm
- `bellman_ford(graph, start)` - Bellman-Ford Algorithm
- `prim(graph, start)` - Prim's Algorithm (Minimum Spanning Tree)
- `kruskal(graph)` - Kruskal's Algorithm (Minimum Spanning Tree)
- `floyd_warshall(graph)` - Floyd-Warshall Algorithm
- `topological_sort(graph)` - Topological Sorting

---

## Tree Algorithms
- `inorder_traversal(root)` - Inorder Traversal
- `preorder_traversal(root)` - Preorder Traversal
- `postorder_traversal(root)` - Postorder Traversal
- `level_order_traversal(root)` - Level Order Traversal (BFS for Trees)

---

## Evolutionary and Optimization Algorithms
- `genetic_algorithm(...)` - Genetic Algorithm
- `simulated_annealing(...)` - Simulated Annealing
- `particle_swarm_optimization(...)` - Particle Swarm Optimization (PSO)
- `differential_evolution(...)` - Differential Evolution
- `ant_colony_optimization(...)` - Ant Colony Optimization (ACO)
- `memetic_algorithm(...)` - Memetic Algorithm
- `artificial_bee_colony(...)` - Artificial Bee Colony Optimization (ABC)
- `harmony_search(...)` - Harmony Search
- `cultural_algorithm(...)` - Cultural Algorithm
- `tabu_search(...)` - Tabu Search

---

## Key Features
- **Real-Time Visualizations:** Step-by-step execution for better understanding.
- **Graph Integration:** Supports visualization of graph-based algorithms using `networkx`.
- **Customizable API:** Adapt algorithm execution and visualizations to your needs.
- **Educational Focus:** Ideal for teaching and learning.

This comprehensive set of algorithms makes `py_visual_algo` a versatile library for various applications, including education, research, and development.

## Installation
```bash
pip install py-visual-algo
```
## Usage

Example of visualizing Bubble Sort:
```bash
from py_visual_algo.algorithms.sorting import bubble_sort
from py_visual_algo.visualizer.plotter import plot_sorting

data = [10, 3, 7, 2, 5]
generator = bubble_sort(data)
plot_sorting(generator)
```
## Running Examples

The `py_visual_algo` library includes a variety of examples to demonstrate its capabilities. These examples are located in the `examples/` directory.

### Steps to Run Examples

1. Clone the repository:
```bash
git clone https://github.com/tirotir-ir/py_visual_algo.git
cd py_visual_algo
```
2. Navigate to the examples/ directory:

```bash
cd examples
```
‍‍‍‍‍‍‍3. Run an example script:
‍‍‍
```bash
    python sorting1.py
```

## Available Examples

- Sorting Algorithms: Demonstrates sorting algorithms like Bubble Sort, Merge Sort, and Quick Sort.
    bubble_sort1.py
- Searching Algorithms: Shows Linear Search, Binary Search, and Jump Search.
    linear_search.py
- Graph Algorithms: Visualizes BFS, DFS, Dijkstra, and A* algorithms.
    graph1.py
- Tree Traversals: Explores Inorder, Preorder, and Postorder traversals.
    tree_traversal1.py
- Optimization Algorithms: Demonstrates Particle Swarm Optimization, Ant Colony Optimization, and more.
    ant_colony_optimization.py

examples/
├── sorting/
│   ├── bubble_sort1.py
│   ├── bubble_sort2.py
│   ├── quick_sort.py
│   ├── merge_sort.py
│   ├── sorting1.py
│   └── sorting2.py
├── searching/
│   ├── linear_search.py
│   ├── binary_search.py
│   ├── jump_search.py
│   └── searching1.py
├── graph_algorithms/
│   ├── a_star1.py
│   ├── bellman_ford.py
│   ├── bfs1.py
│   ├── bfs_with_edges.py
│   ├── dfs1.py
│   ├── dfs_with_edges.py
│   ├── dijkstra1.py
│   ├── dijkstra2.py
│   ├── graph1.py
│   ├── graph2.py
│   └── graph3.py
├── tree_algorithms/
│   ├── inorder_traversal.py
│   ├── postorder_traversal.py
│   ├── preorder_traversal.py
│   ├── tree_traversal1.py
│   └── tree_traversal2.py
├── evolutionary_algorithms/
│   ├── ant_colony_optimization.py
│   ├── artificial_bee_colony.py
│   ├── cultural_algorithm.py
│   ├── differential_evolution.py
│   ├── genetic_algorithm.py
│   ├── harmony_search.py
│   ├── memetic_algorithm.py
│   ├── pso_example.py
│   ├── simulated_annealing.py
│   └── evolutionary1.py
└── pathfinding/
    ├── pathfinding1.py
    └── pathfinding2.py


# Using the Graphical User Interface (GUI)

The `py_visual_algo` library includes a user-friendly Graphical User Interface (GUI) to browse and run examples interactively. Follow these steps to use the GUI:

---

## **Steps to Run the GUI**

### **1. Activate the Virtual Environment**

Activate your virtual environment to use the installed library:

- On **Windows**:
  ```bash
  <virtual_env_root>\Scripts\activate
  ```
- Example:
  ```bash
  python -m venv env
  env\Scripts\activate
  ```

- On **macOS/Linux**:
  ```bash
  source <virtual_env_root>/bin/activate
  ```
---

### **2. Install the Library (if not already installed)**

If the library is not already installed in the virtual environment, install it using pip:

  ```bash
pip install py_visual_algo
  ```

Ensure the examples folder is either included in the installed package or downloaded separately there (see Step 3).

---

### **3. Ensure the `examples` Folder is in the Correct Location**

The `examples` folder must be located two levels above the GUI script (`gui.py`). If the library is installed in a virtual environment, place the `examples` folder under:

```plaintext
<virtual_env_root>/Lib/site-packages/examples
```

For example, in a typical virtual environment, the directory structure should look like this:

```plaintext
<virtual_env_root>/
├── Lib/
│   ├── site-packages/
│   │   ├── py_visual_algo/
│   │   │   ├── ui/
│   │   │   │   └── gui.py
│   │   ├── examples/
│   │   │   ├── bfs1.py
│   │   │   ├── bubble_sort1.py
│   │   │   └── ...
```

Move the `examples` folder to the correct location by running:

```bash
move <path_to_downloaded_examples> <virtual_env_root>/Lib/site-packages/
```

---

### **4. Run the GUI**

Once the directory structure is correct and the virtual environment is active, run the GUI:

```bash
python -m py_visual_algo.ui.gui
```

---

### **5. Select and Run Examples**

When the GUI launches:
- It will dynamically load available examples from the `examples` folder.
- Select an example from the list displayed in the GUI.
- Click **Run Example** to execute it.

Ensure the `examples` folder contains valid Python files (e.g., `bfs1.py`, `bubble_sort1.py`). The output or visualization will appear after the example runs successfully.


---

## **Running Examples Separately**

If you prefer to run examples individually without using the GUI, follow these steps:

### **Find the Example Files**
The `examples` folder contains Python scripts for various algorithms. Ensure the `examples` folder is downloaded and placed in the correct location:
```plaintext
<virtual_env_root>/Lib/site-packages/examples
```

---

### **3. Run an Example**
Navigate to the `examples` folder and execute any example script directly. For example:

- **Run BFS Example**:
  ```bash
  python <virtual_env_root>/Lib/site-packages/examples/bfs1.py
  ```

- **Run Bubble Sort Example**:
  ```bash
  python <virtual_env_root>/Lib/site-packages/examples/bubble_sort1.py
  ```

Replace `<virtual_env_root>` with the path to your virtual environment.

---

## **Troubleshooting**

1. **No Examples Displayed in the GUI**:
   - Verify the `examples` folder is in the correct location (`<virtual_env_root>/Lib/site-packages/examples`).
   - Confirm the `examples` folder contains `.py` files.

2. **Virtual Environment Not Activated**:
   - Ensure the virtual environment is activated before running the GUI or examples.

By following these steps, you can explore and run the library's examples interactively or individually.


## Contributing

See CONTRIBUTING.md for guidelines.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
