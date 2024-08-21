# Merge sort algorithm
# Best-case time complexity: O(n log n)
# Worst-case time complexity: O(n log n)
# Average-case time complexity: O(n log n)
# Time complexity: O(n log n) for all cases
# Space complexity: O(n)
# Stable: Yes
# Method: Merging   
# Type: Deterministic
# In-place: No
# Note: This algorithm is a basic version of the merge sort algorithm.

from sorting.merge import merge

def merge_sort(A, p, r):
    """
    Input:
        A: list of integers
        p: starting index of A
        r: ending index of A
    
    Output: non-decreasing sorted list of A
    """
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)
        merge_sort(A, q + 1, r)
        merge(A, p, q, r)
    return A
