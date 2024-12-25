def bubble_sort(arr):
    """
    Bubble Sort implementation.

    Args:
        arr (list): List of elements to be sorted.

    Yields:
        list: Current state of the list after each pass.
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        yield arr


def merge_sort(arr):
    """
    Merge Sort implementation.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


def merge(left, right):
    """
    Merge two sorted lists.

    Args:
        left (list): Left sublist.
        right (list): Right sublist.

    Returns:
        list: Merged sorted list.
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    Quick Sort implementation.

    Args:
        arr (list): List of elements to be sorted.

    Returns:
        list: Sorted list.
    """
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
