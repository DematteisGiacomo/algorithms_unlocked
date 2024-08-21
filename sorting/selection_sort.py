# Selection sort algorithm
# Best-case time complexity: O(n^2)
# Worst-case time complexity: O(n^2)
# Average-case time complexity: O(n^2)
# Space complexity: O(1)
# Stable: No
# Method: Selection
# Type: Deterministic
# In-place: Yes
# Note: This algorithm is a basic version of the selection sort algorithm.

def selection_sort(A, n):
    """
    Inputs:
        A: list of integers
        n: number of elements in A

    Output: sorted list of A
    """
    for i in range(n - 1):
        smallest = i
        for j in range(i+1, n):
            if A[j] < A[smallest]:
                smallest = j
        A[i], A[smallest] = A[smallest], A[i]
    return A
