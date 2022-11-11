a = {}
b = {}
A = input()
B = input()
aminus = []
bminus = []
for i in A :
    i = i.lower()
    if i.isalpha() :
        if i not in a :
            a[i] = 1
        else :
            a[i] += 1
for i in B :
    i = i.lower()
    if i.isalpha() :
        if i not in b :
            b[i] = 1
        else :
            b[i] += 1
for i in a :
    if i not in b :
        aminus.append([i, a[i]])
    elif a[i] <= b[i] :
        continue
    else :
        aminus.append([i, a[i] - b[i]])
for i in b :
    if i not in a :
        bminus.append([i, b[i]])
    elif b[i] <= a[i] :
        continue
    else :
        bminus.append([i, b[i] - a[i]])
aminus = sorted(aminus)
bminus = sorted(bminus)
print(A)
if aminus == [] :
    print(" - None")
else :
    for i in aminus :
        if i[1] == 1 :
            print(" - remove {} {}".format(i[1], i[0]))
        elif i[1] > 1 :
            print(" - remove {} {}'s".format(i[1], i[0]))
print(B)
if bminus == [] :
    print(" - None")
else :
    for i in bminus :
        if i[1] == 1 :
            print(" - remove {} {}".format(i[1], i[0]))
        elif i[1] > 1 :
            print(" - remove {} {}'s".format(i[1], i[0]))