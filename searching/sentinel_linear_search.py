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
def linear_search(A, n, x):
    """
    Inputs:
        A: list of integers
        n: number of elements in A
        x: integer to search

    Output: index of x in A, -1 if x is not in A
    """
    for i in range(n):
        if A[i] == x:
            return i
    return -1
