n = int(input())


for e in range(0, n) :
    data = input().split(" ")
    if e == 0 :
        x = [int(data[0])]
        y = [int(data[1])]
    else :
        x += [int(data[0])]
        y += [int(data[1])]

method = 0
invert = input()

if invert == "Zag-Zig" :
    method = 1

line1 = x[::2] + y[1::2]
line2 = x[1::2] + y[::2]

if method == 0 :
    print(min(line1), max(line2))
if method == 1 :
    print(min(line2), max(line1))