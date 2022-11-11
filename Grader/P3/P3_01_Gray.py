n = int(input())
k = int(input())
if n < 1 and k < 1 :
    print("Invalid n and k")
elif n < 1 :
    print("Invalid n")
elif k < 1 :
    print("Invalid k")
else :
    x = ["0","1"]
    z = list()
    for i in range(1,n) :
        y = x.copy()
        y.reverse()
        for i in range(len(x)) :
            x[i] = "0"+x[i]
            y[i] = "1"+y[i]
        x += y
    for i in range(1, k+1) :
        i = str(i)
        while len(str(i)) < n+1 :
            i += "-"
        z.append(i)
    z[-1] = z[-1][0:-1]
    print("".join(z))
    while x != [] :
        if len(x) > k :
            print(",".join(x[0:k]))
            x = x[k:]
        elif len(x) <= k :
            print(",".join(x))
            x = []