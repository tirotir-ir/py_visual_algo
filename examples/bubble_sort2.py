from py_visual_algo.algorithms.sorting import bubble_sort

data = [5, 3, 8, 6, 2]
print("Original Data:", data)

for step in bubble_sort(data):
    print("Sorting Step:", step)

print("Sorted Data:", data)
