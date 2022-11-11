data = {}
while True :
    x = input()
    if x == "q" :
        break
    x = x.split(", ")
    if x[1] not in data :
        data[x[1]] = x[0]
    else :
        data[x[1]] += ", " + x[0]
listed = []
for i in data :
    listed += [i]
listed.sort()
for i in listed :
    print(i + ": " + data[i])