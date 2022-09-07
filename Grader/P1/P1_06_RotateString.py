mode = input()
line = int(input())
data = []
sent = []
status = 1
for i in range(line) :
    data += [list(input().strip())]

if len(data) == 1 :
    pass
elif len(data) > 1 :
    for i in range(1,line) :
        if len(data[i]) == len(data[i - 1]) :
            pass
        elif len(data[i]) != len(data[i - 1]) :
            print("Invalid size")
            status = 0
            break

if status == 1 and mode == "90" :
    for i in range(len(data[0])) :
        for e in range(line) :
            sent += [data[e][i]]
        print("".join(sent[::-1]))
        sent = []

if status == 1 and mode == "flip" :
    for i in range(line) :
        print("".join(data[i][::-1]))

if status == 1 and mode == "180" :
    for i in range(line) :
        print("".join(data[(line - 1) - i][::-1]))