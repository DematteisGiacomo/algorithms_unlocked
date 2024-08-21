# Quick sort algorithm
# Best-case time complexity: O(n log n)
# Worst-case time complexity: O(n^2)
# Average-case time complexity: O(n log n)
# Time complexity: O(n log n) for all cases
# Space complexity: O(log n)
# Stable: No
# Method: Partitioning
# Type: Deterministic
# In-place: Yes
# Note: This algorithm is a basic version of the quick sort algorithm.

from sorting.partition import partition

def quicksort(A, p, r):
    """
    Input:
        A: list of integers
        p: starting index of A
        r: ending index of A
    
    Output: non-decreasing sorted list of A
    """
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)
    return A
