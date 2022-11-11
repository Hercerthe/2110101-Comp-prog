import numpy as np
def eq(A, B, p):
    x = np.sum(A == B)
    y = np.sum(A == A)
    return (x/y) >= p/100
def closest_point_indexes(points, p):
    x = ((points[: , 0]-p[0])**2)+((points[: , 1]-p[1])**2)
    return np.arange(x.shape[0])[x == np.min(x)]
def number_of_inversions(A):
    n = 0
    l = 1
    for i in A :
        x = i > A[l:]
        n += np.sum(x)
        l += 1
    return n
exec(input().strip())