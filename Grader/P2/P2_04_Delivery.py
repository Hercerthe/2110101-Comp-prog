time = {"E":1, "Q":3, "N":7, "F":14}
data = []
while True :
    order = input().split()
    if "END" in order :
        break
    t,d,m,y = order[1],int(order[2]),int(order[3]),int(order[4]) - 543
    if y + 543 < 2558 :
        print("Error: {} --> Invalid year".format(" ".join(order)))
        continue
    if m not in range(1,13) :
        print("Error: {} --> Invalid month".format(" ".join(order)))
        continue
    if d not in range(1,32) :
        print("Error: {} --> Invalid date".format(" ".join(order)))
        continue
    if m in [4,6,9,11] and d > 30 :
        print("Error: {} --> Invalid date".format(" ".join(order)))
        continue
    if m == 2 :
        if ((y%400 == 0) or (y%4 == 0 and y%100 != 0)) :
            if d > 29 :
                print("Error: {} --> Invalid date".format(" ".join(order)))
                continue
            else :
                pass
        elif d > 28 :
            print("Error: {} --> Invalid date".format(" ".join(order)))
            continue
    if t not in time :
        print("Error: {} --> Invalid delivery type".format(" ".join(order)))
        continue
    d += time[t]
    if m in [1,3,5,7,8,10,12] and d > 31 :
        d -= 31
        m += 1
    elif m in [4,6,9,11] and d > 30 :
        d -= 30
        m += 1
    elif m == 2 and ((y%400 == 0) or (y%4 == 0 and y%100 != 0)) and d > 29 :
        d -= 29
        m += 1
    elif m == 2 and d > 28 :
        d -= 28
        m += 1
    if m > 12 :
        m -= 12
        y += 1
    y += 543
    data.append([y,m,d,order[0]])
data = sorted(data)
for i in data :
    print("{}: delivered on {}/{}/{}".format(i[3], i[2], i[1], i[0]))