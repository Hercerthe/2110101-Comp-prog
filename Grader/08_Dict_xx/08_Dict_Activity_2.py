n = int(input())
pizza = {
    "PZ871":265.25,
    "PZ953":246.50,
    "Z1983":256.50,
    "Z2853":272.50,
    "LC673":309.25
}
data = {}
for i in range(n) :
    x = input().split(",")
    if x[0] not in data :
        data[x[0]] = 0
    for i in range(len(x)) :
        if x[i] in pizza :
            data[x[0]] += pizza[x[i]]*int(x[i+1])
listed = []
for i in data :
    listed += [i]
listed.sort()
for i in listed :
    print(i + " -> " + str(round(data[i], 2)))