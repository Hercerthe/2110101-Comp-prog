name = [["Robert","Dick"],["William","Bill"],["James","Jim"],["John","Jack"],["Margaret","Peggy"],["Edward","Ed"],["Sarah","Sally"],["Andrew","Andy"],["Anthony","Tony"],["Deborah","Debbie"]]
line = int(input())
input_name = []

for i in range(line) :
    input_name += [input()]


for e in range(line) :
    for i in range(10) :
        if input_name[e] in name[i] :
            if input_name[e] == name[i][0] :
                print(name[i][1])
                break
            else :
                print(name[i][0])
                break
        elif i == 9 :
            print("Not found")
            break