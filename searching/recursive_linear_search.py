# Recursive linear search algorithm
# Best-case time complexity: O(1)
# Worst-case time complexity: O(n)
# Average-case time complexity: O(n)
# Space complexity: O(n)
# Stable: Yes
# Method: Linear search
# Type: Deterministic
# In-place: No
# Note: This algorithm is a recursive version of the linear search algorithm.

def recursive_lines_search(A,n,i,x):
    """
    Inputs:
        A: list of integers
        n: number of elements in A
        x: integer to search

    Output: index of x in A, -1 if x is not in A
    """
    if i > n - 1:
        return -1
    elif A[i] == x:
        return i
    else:
        return recursive_lines_search(A,n,i+1,x)
