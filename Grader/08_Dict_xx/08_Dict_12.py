data = {}
for i in range(int(input())) :
    ram = input().split()
    data[" ".join(ram[0:2])] = ram[2]
    data[ram[2]] = " ".join(ram[0:2])
for i in range(int(input())) :
    look = input()
    if look in data :
        print(look, "-->", data[look])
    else :
        print(look, "--> Not found")