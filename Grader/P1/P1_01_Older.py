p1 = input().split(", ")
p2 = input().split(", ")
n1,m1,d1 = p1[0].split(" ")
n2,m2,d2 = p2[0].split(" ")
y1 = p1[1]
y2 = p2[1]
month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
x = 1
y = 1

for e in month :
    if m1 == e :
        m1 = x
    if m2 == e :
        m2 = y
    x += 1
    y += 1

if int(y1) > int(y2) :
    print(n2)
elif int(y1) < int(y2) :
    print(n1)
elif m1 > m2 :
    print(n2)
elif m1 < m2 :
    print(n1)
elif int(d1) > int(d2) :
    print(n2)
elif int(d1) < int(d2) :
    print(n1)
else :
    print(n1, n2)