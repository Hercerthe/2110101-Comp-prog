data = dict()
for i in range(int(input())) :
    x = input().split(", ")
    for j in range(1,len(x)) :
        if x[j] not in data :
            data[x[j]] = list()
        data[x[j]].append(x[0])
for i in input().split(", ") :
    if i not in data :
        print("{} -> Not found".format(i))
    else :
        print("{} -> {}".format(i, ", ".join(data[i])))