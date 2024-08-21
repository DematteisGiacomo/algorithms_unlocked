# Partition procedure

def partition(A, p, r):
    """
    Input:
        A: list of integers
        p: starting index of A
        r: ending index of A

    Output: return the index of the pivot element
    """
    q = p
    for u in range(p, r):
        if A[u] <= A[r]:
            A[q], A[u] = A[u], A[q]
            q += 1
    A[q], A[r] = A[r], A[q]
    return q
