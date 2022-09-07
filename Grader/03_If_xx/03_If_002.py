d,m,y = [int(e) for e in input().split()]

y -= 543
n = 31

if m == 4 or m == 6 or m == 9 or m == 11 :
    n = 30
    pass
else :
    if m == 2 :
        n = 28

        if y % 400 == 0 :
            n = 29
            pass

        if y % 4 == 0 and y % 100 != 0 :
            n = 29
            pass

        else :
            pass
        pass

    else :
        pass
    pass

d += 15

if d > n :
    d -= n
    m += 1
    pass

if m > 12 :
    m -= 12
    y += 1
    pass

y += 543

print(str(d) + "/" + str(m) + "/" + str(y))