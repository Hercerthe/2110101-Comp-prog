cartoon = {}
sort = []
while True :
    x = input()
    if x == "q" :
        break
    x = x.split(", ")
    if x[1] not in cartoon :
        cartoon[x[1]] = [x[0]]
    else :
        cartoon[x[1]].append(x[0])
    if x[1] not in sort :
        sort.append(x[1])
for i in sort :
    print("{}: {}".format(i, ", ".join(cartoon[i])))