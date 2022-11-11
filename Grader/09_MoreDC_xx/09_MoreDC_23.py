genre = {}
top3 = []
for i in range(int(input())) :
    x = input().strip().split(", ")
    time = (int(x[-1].split(":")[0])*60)+(int(x[-1].split(":")[1]))
    if x[-2] not in genre :
        genre[x[-2]] = time
    else :
        genre[x[-2]] += time
for i in genre :
    top3.append([genre[i], i])
top3 = sorted(top3, reverse=True)
for i in top3[:3] :
    s = i[0]%60
    if len(str(s)) == 1 :
        s = "0"+str(s)
    print("{} --> {}:{}".format(i[1], i[0]//60, s))