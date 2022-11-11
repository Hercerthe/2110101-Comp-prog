def pattern1(nrows, ncols):
    s = 1
    x = []
    for i in range(nrows) :
        y = []
        for e in range(ncols) :
            y.append(s)
            s += 1
        x.append(y)
    return x
def pattern2(nrows, ncols):
    x = []
    s = 1
    for i in range(nrows) :
        x.append([])
    for i in range(ncols) :
        for e in range(nrows) :
            x[e].append(s)
            s += 1
    return x
def pattern3(N):
    if N == 0 :
        return []
    x = []
    y = []
    s = 1
    for i in range(N) :
        while len(y) < i :
            y.append(0)
        while len(y) < N :
            y.append(s)
            s += 1
        x.append(y)
        y = []
    return x
def pattern4(N):
    if N == 0 :
        return []
    x = []
    s = 1
    for i in range(N) :
        x.append([])
    for i in range(N) :
        for e in range(i) :
            x[i].append(0)
    for i in range(N) :
        while i != -1 :
            x[i].append(s)
            s += 1
            i -= 1
    return x
def pattern5(N):
    if N == 0 :
        return []
    x = []
    s = 1
    for i in range(N) :
        x.append([])
    for i in range(N) :
        for e in range(i) :
            x[i].append(0)
    while len(x[0]) < N :
        for i in range(N) :
            if len(x[i]) < N :
                x[i].append(s)
                s += 1
    return x
def pattern6(N):
    if N == 0 :
        return []
    x = []
    s = 1
    for i in range(N) :
        x.append([])
    for i in range(N) :
        for e in range(i) :
            x[i].append(0)
    while len(x[0]) < N :
        for i in range(N) :
            if len(x[i]) < N :
                x[i].append(s)
                s += 1
        for i in range(N-1,-1,-1) :
            if len(x[i]) < N :
                x[i].append(s)
                s += 1
    return x
exec(input().strip())