p = float(input())
k = 1
t = 1

t = (t*(365 - (k - 1)))/365

while not 1 - t >= p :
    t = (t*(365 - (k - 1)))/365
    if 1 - t >= p :
        break
    k += 1

print(k)