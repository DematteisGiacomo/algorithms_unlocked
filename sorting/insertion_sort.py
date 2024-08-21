# Insertion sort algorithm
# Best-case time complexity: O(n)
# Worst-case time complexity: O(n^2)
# Average-case time complexity: O(n^2)
# Space complexity: O(1)
# Stable: Yes
# Method: Insertion
# Type: Deterministic
# In-place: Yes
# Note: This algorithm is a basic version of the insertion sort algorithm.

def insertion_sort(A, n):
    """
    Inputs:
        A: list of integers
        n: number of elements in A

    Output: sorted list of A
    """
    for i in range(1, n):
        key = A[i]
        j = i - 1
        while j >= 0 and key < A[j]:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
    return A
