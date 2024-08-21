# Recursive binary search algorithm
# Best case: O(1)
# Worst case: O(log(n))
# Average case: O(log(n))
# Space complexity: O(log(n))
# Stable: Yes
# Method: Binary search
# Type: Deterministic
# In-place: No
# Note: This algorithm is a recursive version of the binary search algorithm.

def recursive_binary_search(A, p, r, x):
    """
    Inputs:
        A: list of ordered in increasing order integers
        p: starting index of A
        r: ending index of A
        x: integer to search
        

    Output: index of x in A, -1 if x is not in A
    """
    if p > r:
        return -1
    q = (p+r)//2 # floor((p+r)/2)
    if A[q] == x:
        return q
    elif A[q] > x:
        return recursive_binary_search(A,p,q-1,x)
    else:
        return recursive_binary_search(A,q+1,r,x)
