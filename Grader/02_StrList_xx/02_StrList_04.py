m = input()
n = int(input())

if len(m) < n :
    print(("0"*(n - len(m))) + m)
else :
    print(m)