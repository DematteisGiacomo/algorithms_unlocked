# Binary search algorithm
# Best case: O(1)
# Worst case: O(log(n))
# Average case: O(log(n))
# Space complexity: O(1)
# Stable: Yes
# Method: Binary search
# Type: Deterministic
# In-place: Yes
# Note: This algorithm is a basic version of the binary search algorithm.

def binary_search(A, n, x):
    """
    Inputs:
        A: list of ordered in increasing order integers
        n: number of elements in A
        x: integer to search

    Output: index of x in A, -1 if x is not in A
    """
    p = 0
    r = n
    while p <= r:
        q = floor((p+r)/2)
        if A[q] == x:
            return q
        elif A[q] > x:
            r = q - 1
        else:
            p = q + 1
    return -1
