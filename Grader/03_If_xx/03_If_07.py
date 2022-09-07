sub = int(input())

if sub < 1000 :
    print(sub)
if 1000 <= sub < 10000 :
    print(str(round(sub / 1000, 1)) + "K")
if 10000 <= sub < 1000000 :
    print(str(round(sub / 1000)) + "K")
if 1000000 <= sub < 10000000 :
    print(str(round(sub / 1000000, 1)) + "M")
if 10000000 <= sub < 1000000000 :
    print(str(round(sub / 1000000)) + "M")
if 1000000000 <= sub < 10000000000 :
    print(str(round(sub / 1000000000, 1)) + "B")
if 10000000000 <= sub :
    print(str(round(sub / 1000000000)) + "B")