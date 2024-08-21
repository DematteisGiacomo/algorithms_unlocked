# Merge procedure

def merge(A, p, q, r):
    """
    Inputs:
        A: list of integers
        p: starting index of A
        q: index somewhere in A
        r: ending index of A
        Note: subarrays A[p..q] and A[q+1..r] are sorted

    Output:
        A: sorted list of A
    """
    n1 = q - p + 1
    n2 = r - q
    B = [0] * n1
    C = [0] * n2
    for i in range(n1):
        B[i] = A[p + i]
    for j in range(n2):
        C[j] = A[q + j + 1]
    B[n1] = float('inf') #positvie infinity
    C[n2] = float('inf')
    i = 0
    j = 0
    for k in range(p, r + 1):
        if B[i] <= C[j]:
            A[k] = B[i]
            i += 1
        else:
            A[k] = C[j]
            j += 1
    return A
