def factor(N):
    data = {}
    fac = []
    k = 2
    while N >= k :
        if N % k == 0 :
            N //= k
            if k in data :
                data[k] += 1
            else :
                data[k] = 1
        else :
            k += 1
    for i in data :
        fac += [[i, data[i]]]
    return sorted(fac)
exec(input().strip())