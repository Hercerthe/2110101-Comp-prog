data = list()
mode = ["LSTRIP", "RSTRIP", "STRIP", "STRIP_ALL"]
func = str()
for i in open(input(), "r") :
    data.append(list(i.replace("\n", "")))
    n = len(i.replace("\n", ""))
func = input().strip()
if func not in mode :
    print("Invalid command")
else :
    for i in range(n) :
        state = True 
        for e in range(len(data)) :
            if data[e][i] != "." :
                state = False
        if state :
            for e in range(len(data)) :
                data[e][i] = " "
    for i in range(len(data)) :
        data[i] = "".join(data[i])
    if func == "LSTRIP" :
        for i in data :
            print(i.lstrip().replace(" ", "."))
    elif func == "RSTRIP" :
        for i in data :
            print(i.rstrip().replace(" ", "."))
    elif func == "STRIP" :
        for i in data :
            print(i.strip().replace(" ", "."))
    elif func == "STRIP_ALL" :
        for i in data :
            print(i.replace(" ", ""))