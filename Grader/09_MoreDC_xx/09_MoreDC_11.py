for i in range(int(input())) :
    count = 0
    x = input()
    if x == "" :
        print(x)
        continue
    while x[count] == "." :
        count += 1
    count //= 2
    print(x[count:])