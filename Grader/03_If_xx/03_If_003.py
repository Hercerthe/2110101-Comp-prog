a,b,c,d = [int(e) for e in input().split()]

if a > b :
    a,b = b,a
    if d >= a :
        if c > d :
            c -= a
            pass
        pass
    else :
        c += a
        pass

    b = a+c+d
    pass

else :
    if c > a >= b :
        d += a
        pass
    else :
        pass
    if d > c :
        b += 2
        pass
    else :
        b *= 2
        pass
    pass

print(a,b,c,d)