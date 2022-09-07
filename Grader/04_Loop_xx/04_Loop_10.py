a = float(input())
b = a
L = 0
U = 0

while b != 0 :
    b //= 10
    U += 1

x = (L + U) / 2

while abs(a - (10**x)) > (10**(-10)) * max(a,10**x) :
    if 10**x > a :
        U = x
    if 10**x < a :
        L = x
    x = (L + U) / 2

print(round(x, 6))