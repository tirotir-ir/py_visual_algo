from py_visual_algo.algorithms.sorting import bubble_sort
from py_visual_algo.visualizer.plotter import plot_sorting

data = [5, 3, 8, 6, 2]
print("Original data:", data)

# Generate the sorting steps
generator = bubble_sort(data)

# Visualize the sorting process
plot_sorting(generator)
print("Sorted data:", data)
