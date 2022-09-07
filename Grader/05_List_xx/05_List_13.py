set = []
k = 0

line = int(input())
for i in range(line) :
    if k % 2 == 0 :
        set += [int(input())]
    elif k % 2 == 1 :
        set = [int(input())] + set
    k += 1

ram = input()
if len(ram) != 0 :
    ram = [int(e) for e in ram.split(" ")]
for i in range(len(ram)) :
    if k % 2 == 0 :
        set += [ram[i]]
    elif k % 2 == 1 :
        set = [ram[i]] + set
    k += 1

while 1 == 1 :
    ram = int(input())
    if ram != -1 :
        if k % 2 == 0 :
            set += [ram]
        elif k % 2 == 1 :
            set = [ram] + set
    elif ram == -1 :
        break
    k += 1

print(set)