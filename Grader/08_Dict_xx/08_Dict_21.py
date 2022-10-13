data = input().lower()
dic = {}
for i in data :
    if not i.isalpha():
        continue
    elif i not in dic :
        dic[i] = 1
    else :
        dic[i] += 1
data = []
for i in dic :
    data += [[-dic[i], i]]
data = sorted(data)
for i in data :
    print(i[1], "->", abs(i[0]))