def first_fit(L,e):
    x = -1
    for i in range(len(L)) :
        if sum(L[i])+e <= 100 :
            x = i
            break
    if x == -1 :
        L.append([e])
    else :
        L[x].append(e)
    return L
def best_fit(L,e):
    x = 0
    y = 0
    for i in range(len(L)) :
        if sum(L[i]) > y and sum(L[i]) + e <= 100 :
            y = sum(L[i])
            x = i
    if y == 0 :
        L.append([e])
    else :
        L[x].append(e)
    return L
def partition_FF(D):
    x = []
    x.append([D[0]])
    D = D[1:]
    for i in D :
        x = first_fit(x, i)
    return x
def partition_BF(D):
    x = []
    x.append([D[0]])
    D = D[1:]
    for i in D :
        x = best_fit(x, i)
    return x
exec(input().strip())