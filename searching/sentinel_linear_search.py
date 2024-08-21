# Sentinel inear search algorithm
# Best-case time complexity: O(1)
# Worst-case time complexity: O(n)
# Average-case time complexity: O(n)
# Space complexity: O(1)
# Stable: Yes
# Method: Linear search
# Type: Deterministic
# In-place: Yes
# Note: This algorithm is a modified version of the linear search algorithm.
# The sentinel linear search algorithm uses a sentinel value to reduce the number of comparisons.
# The sentinel value is placed at the end of the list, and the loop is terminated when the sentinel value is found.

def sentinel_linear_search(A, n, x):
    """
    Inputs:
        A: list of integers
        n: number of elements in A
        x: integer to search

    Output: index of x in A, -1 if x is not in A
    """
    last = A[n - 1]
    A[n - 1] = x
    i = 0
    while A[i] != x:
        i += 1
    A[n - 1] = last
    if i < n - 1 or A[n - 1] == x:
        return i
    return -1
