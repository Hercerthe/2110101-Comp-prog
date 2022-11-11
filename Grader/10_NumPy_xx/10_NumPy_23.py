import numpy as np
def read_data():
    w = [float(e) for e in input().split()]
    weight = np.array(w)
    n = int(input())
    data = np.ndarray((n, 4), int)
    for i in range(n):
        data[i] = [int(e) for e in input().split()]
    return weight, data
def report_lower_than_mean(weight, data):
    data[: , 1] = np.sum(data[: , 1:] * weight, axis=1)
    data = data[: , :2]
    data[: , 1] = data[: , 1] < np.average(data[: , 1])
    x = [str(i) for i in data[: , 0][data[: , 1] == 1]]
    if x == list() :
        print(None)
    else :
        print(", ".join(x))
exec(input().strip())