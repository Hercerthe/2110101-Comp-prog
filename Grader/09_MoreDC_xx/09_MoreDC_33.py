def add_poly(p1, p2):
    d = dict()
    for i in p1 :
        d[i[1]] = i[0]
    for i in p2 :
        if i[1] in d :
            d[i[1]] += i[0]
        else :
            d[i[1]] = i[0]
    l1 = list()
    l2 = list()
    for i in d :
        if d[i] != 0 :
            l1.append((i, d[i]))
    l1 = sorted(l1, reverse=True)
    for i in l1 :
        x,y = i
        l2.append((y,x))
    return l2
def mult_poly(p1, p2):
    d = dict()
    l1 = list()
    l2 = list()
    for i in p1 :
        for e in p2 :
            if i[1]+e[1] not in d :
                d[i[1]+e[1]] = i[0]*e[0]
            elif i[1]+e[1] in d :
                d[i[1]+e[1]] += i[0]*e[0]
    for i in d :
        l1.append((i, d[i]))
    l1 = sorted(l1, reverse=True)
    for i in l1 :
        x,y = i
        l2.append((y,x))
    return l2
for i in range(3):
    exec(input().strip())