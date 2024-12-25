from py_visual_algo.algorithms.sorting import bubble_sort

data = [64, 34, 25, 12, 22, 11, 90]
generator = bubble_sort(data)

for step in generator:
    print(step)
