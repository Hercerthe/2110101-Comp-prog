data = []
for i in range(int(input())) :

    x = input().split(" ")
    y = []
    for i in x :
        if i != "" :
            y.append(i)
    data.append(y)
mode = input().split(" ")
if "show" in mode :
    for i in data :
        print(" ".join(i))
elif "get" in mode :
    x = []
    for i in data :
        if i[0] == mode[-1] :
            x = i
    if x == [] :
        x = [mode[-1], "not found"]
    print(" ".join(x))
elif "avg" in mode :
    x = []
    for i in data :
        x += [float(i[int(mode[-1])])]
    print(round(sum(x)/len(x), 4))
elif "max" in mode :
    x = []
    for i in data :
        x += [[float("-"+i[int(mode[-1])]), i[0]]]
    x = sorted(x)
    print(x[0][1], str(x[0][0])[1:])
elif "sort" in mode :
    x = []
    y = []
    for i in data :
        x += [[float(i[int(mode[-1])]), i[0]]]
    x = sorted(x)
    for i in x :
        y.append(i[1])
    print(" ".join(y))