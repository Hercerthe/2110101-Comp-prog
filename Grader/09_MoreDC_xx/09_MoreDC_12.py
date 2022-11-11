U = set()
I = set()
for i in range(int(input())) :
    x = set()
    for e in input().split() :
        x.add(e)
    U = U.union(x)
    if i == 0 :
        I = x
    else :
        I = I.intersection(x)
print(len(U))
print(len(I))