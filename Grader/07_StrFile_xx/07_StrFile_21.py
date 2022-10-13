lower1 = "abcdefghijklm"
lower2 = "nopqrstuvwxyz"
upper1 = "ABCDEFGHIJKLM"
upper2 = "NOPQRSTUVWXYZ"

while 1 == 1 :
    data = list(input())
    if data == ["e", "n", "d"] :
        break
    for i in range(len(data)) :
        if data[i] in lower1 :
            data[i] = lower2[lower1.index(data[i])]
        elif data[i] in lower2 :
            data[i] = lower1[lower2.index(data[i])]
        elif data[i] in upper1 :
            data[i] = upper2[upper1.index(data[i])]
        elif data[i] in upper2 :
            data[i] = upper1[upper2.index(data[i])]

    print("".join(data))