data = dict()
bidder = set()
pay = dict()
for i in range(int(input())) :
    x = input().strip().split()
    bidder.add(x[1])
    if x[2] not in data :
        data[x[2]] = dict()
    if x[0] == "B" :
        data[x[2]][x[1]] = [int(x[3]), -len(data[x[2]]), x[1]]
    elif x[0] == "W" :
        data[x[2]][x[1]] = list()
for i in data :
    winner = list()
    for j in data[i] :
        if data[i][j] != list() :
            winner.append(data[i][j])
    winner.sort(reverse=True)
    if winner == list() :
        continue
    if winner[0][2] not in pay :
        pay[winner[0][2]] = [winner[0][0], i]
    else :
        pay[winner[0][2]][0] += winner[0][0]
        pay[winner[0][2]].append(i)
for i in sorted(list(bidder)) :
    if i not in pay :
        print("{}: $0".format(i))
    else :
        print("{}: ${} -> {}".format(i, pay[i][0], " ".join(sorted(pay[i][1:]))))