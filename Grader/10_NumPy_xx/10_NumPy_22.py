import numpy as np
def mult_table(nrows, ncols):
    arr = list()
    for i in range(1,nrows+1) :
        row = list()
        for j in range(1,ncols+1) :
            row.append(i*j)
        arr.append(row)
    return np.array(arr)
exec(input().strip())