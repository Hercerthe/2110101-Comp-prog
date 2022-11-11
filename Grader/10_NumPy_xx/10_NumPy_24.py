import numpy as np
def peak_indexes(x):
    x[1:-1] = (x[1:-1] > x[0:-2]) & (x[1:-1] > x[2:])
    x[0] = 0
    x[-1] = 0
    return np.where(x==1)[0]
def main():
    d = np.array([float(e) for e in input().split()])
    pos = peak_indexes(np.array(d))
    if len(pos) > 0:
        print(", ".join([str(e) for e in pos]))
    else:
        print("No peaks")
exec(input().strip())