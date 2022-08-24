import math

data = input().split(",")

x = int("0"+data[1]+data[2]) - int("0"+data[1])
y = int(("9"*len(data[2]))+("0"*len(data[1])))
z = (int(data[0])*y)//math.gcd(x,y)

print((x//math.gcd(x,y))+z, "/", y//math.gcd(x,y))