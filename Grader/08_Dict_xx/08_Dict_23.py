data = {}
for i in range(int(input())) :
    ram = input().split()
    data[ram[0]] = ram[1]
    data[ram[1]] = ram[0]
for i in range(int(input())) :
    look = input()
    if look in data :
        print(data[look])
    else :
        print("Not found")