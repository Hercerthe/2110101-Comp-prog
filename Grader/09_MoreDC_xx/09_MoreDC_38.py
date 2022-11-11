data = dict()
station = set()
while True :
    x = input().split()
    if len(x) == 1 :
        if x[0] not in data :
            data[x[0]] = set()
        break
    for i in x :
        if i not in data :
            data[i] = set()
    data[x[0]].add(x[1])
    data[x[1]].add(x[0])
station = set(x)
for i in range(2) :
    for e in station :
        station = station.union(data[e])
station = sorted(list(station))
for i in station :
    print(i)