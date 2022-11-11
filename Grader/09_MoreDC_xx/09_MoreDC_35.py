data = dict()
datalist = dict()
for i in range(int(input())) :
    x = input().split()
    data[x[0]] = set(x[1:])
    datalist[x[0]] = x
look = set(input().split())
here = list()
for i in data :
    if look.issubset(data[i]) :
        here.append(datalist[i])
here = sorted(here)
if here == list() :
    print("Not Found")
else :
    for i in here :
        print(" ".join(i))