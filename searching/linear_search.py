# Linear search algorithm
# Best-case time complexity: O(1)
# Worst-case time complexity: O(n)
# Average-case time complexity: O(n)
# Space complexity: O(1)
# Stable: Yes
# Method: Linear search
# Type: Deterministic
# In-place: Yes
# Note: This algorithm is a basic version of the linear search algorithm.
def linear_search(A, n, x):
    """
    Inputs:
        A: list of integers
        n: number of elements in A
        x: integer to search

    Output: index of x in A, -1 if x is not in A
    """
    answer = -1
    for i in range(n):
        if A[i] == x:
            answer = i
            break
    return answer
