vote = dict()
member = set()
while True :
    x = input().strip()
    if x in ["1","2","3"] :
        break
    x = x.split()
    member.add(x[1])
    if x[0] not in vote :
        vote[x[0]] = dict()
    if x[1] not in vote[x[0]] :
        vote[x[0]][x[1]] = 0
    vote[x[0]][x[1]] += int(x[2])
if x == "1" :
    top3 = list()
    data = dict()
    for i in list(member) :
        data[i] = 0
    for i in vote :
        for j in vote[i] :
            data[j] -= vote[i][j]
    for i in data :
        top3.append([data[i], i])
    top3.sort()
    print("{}, {}, {}".format(top3[0][1], top3[1][1], top3[2][1]))
if x == "2" :
    top3 = list()
    data = dict()
    for i in list(member) :
        data[i] = 0
    for i in vote :
        for j in vote[i] :
            data[j] -= 1
    for i in data :
        top3.append([data[i], i])
    top3.sort()
    print("{}, {}, {}".format(top3[0][1], top3[1][1], top3[2][1]))
if x == "3" :
    top3 = list()
    data = dict()
    for i in list(member) :
        data[i] = 0
    for i in vote :
        high = list()
        for j in vote[i] :
            high.append([-vote[i][j], j])
        high.sort()
        data[high[0][1]] -= 1
    for i in data :
        top3.append([data[i], i])
    top3.sort()
    print("{}, {}, {}".format(top3[0][1], top3[1][1], top3[2][1]))