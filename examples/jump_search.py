from py_visual_algo.algorithms.searching import jump_search

data = [2, 4, 6, 8, 10, 12, 14, 16]
target = 10
result = jump_search(data, target)
print(f"Jump Search: Target {target} found at index {result}")
