reference = sorted(input().replace(" ", "").lower())
data = sorted(input().replace(" ", "").lower())

if len(data) != len(reference) :
    print("NO")
else :
    if reference == data :
        print("YES")
    else :
        print("NO")