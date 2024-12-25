from py_visual_algo.algorithms.sorting import bubble_sort, merge_sort
from py_visual_algo.visualizer.plotter import plot_sorting


def run_sorting():
    """Run sorting examples."""
    data = [64, 34, 25, 12, 22, 11, 90]

    print("Bubble Sort:")
    generator = bubble_sort(data.copy())
    for step in generator:
        print(step)

    print("\nMerge Sort:")
    generator = merge_sort(data.copy())
    for step in generator:
        print(step)


def visualize_sorting():
    """Visualize Bubble Sort."""
    data = [64, 34, 25, 12, 22, 11, 90]
    generator = bubble_sort(data.copy())
    print("\nVisualizing Bubble Sort...")
    plot_sorting(generator)


if __name__ == "__main__":
    run_sorting()
    visualize_sorting()
