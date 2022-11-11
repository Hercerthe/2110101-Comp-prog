import numpy as np
def get_column_from_bottom_to_top( A, c ):
    return A[::-1, c]
def get_odd_rows( A ):
    return A[1::2]
def get_even_column_last_row( A ):
    return A[-1 , ::2]
def get_diagonal1( A ):
    b = list()
    for i in range(A.shape[0]) :
        b.append(i)
    return A[b, b]
def get_diagonal2( A ):
    b = list()
    for i in range(A.shape[0]) :
        b.append(i)
    c = b.copy()
    c.reverse()
    return A[b, c]
exec(input().strip())