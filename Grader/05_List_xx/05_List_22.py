data = []
grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]
while True :
    ram = input()
    if ram == "q" :
        break
    data += [ram.split(" ")]
upgrade = input().split()
for i in range(len(data)) :
    if data[i][0] in upgrade :
        for e in range(len(grade)) :
            if data[i][1] == grade[0] :
                break
            elif data[i][1] == grade[e] :
                data[i][1] = grade[e - 1]
data = sorted(data)
for i in range(len(data)) :
    print(" ".join(data[i]))