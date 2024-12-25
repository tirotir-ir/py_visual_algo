def linear_search(arr, target):
    """
    Linear Search implementation.

    Args:
        arr (list): List of elements to search in.
        target: The element to search for.

    Returns:
        int: Index of the target element, or -1 if not found.
    """
    for index, value in enumerate(arr):
        if value == target:
            return index
    return -1


def binary_search(arr, target):
    """
    Binary Search implementation.

    Args:
        arr (list): Sorted list of elements to search in.
        target: The element to search for.

    Returns:
        int: Index of the target element, or -1 if not found.
    """
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def jump_search(arr, target):
    """
    Jump Search implementation.

    Args:
        arr (list): Sorted list of elements to search in.
        target: The element to search for.

    Returns:
        int: Index of the target element, or -1 if not found.
    """
    import math

    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for index in range(prev, min(step, n)):
        if arr[index] == target:
            return index
    return -1
