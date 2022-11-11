data = {}
datalist = []
for i in range(int(input())) :
    x = input().split(": ")
    city = set()
    for e in x[1].split(", ") :
        city.add(e[0])
    data[x[0]] = city
    datalist.append(x[0])
want = input()
state = False
for i in datalist :
    if i != want and not data[i].isdisjoint(data[want]) :
        print(i)
        state = True
if state == False :
    print("Not Found")