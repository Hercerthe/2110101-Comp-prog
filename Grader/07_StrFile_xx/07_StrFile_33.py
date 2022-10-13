data1 = ""
data2 = ""
for i in open("/Users/cookie/Documents/2110101-Comp-prog/Grader/07_StrFile_xx/data1.txt", "r") :
    data1 += i.replace("\n", "")+","
for i in open("/Users/cookie/Documents/2110101-Comp-prog/Grader/07_StrFile_xx/data2.txt", "r") :
    data2 += i.replace("\n", "")+","
data1 = data1.split(",")[0:-1]
data2 = data2.split(",")[0:-1]

for i in range(len(data2)) :
    for e in range(len(data1)) :
        if data1[e][8:10] == data2[i][8:10] :
            if data1[e][0:8] > data2[i][0:8] :
                data1.insert(e, data2[i])
                break
            elif e+1 == len(data1) :
                data1.append(data2[i])
            continue
        elif data1[e][8:10] > data2[i][8:10] :
            data1.insert(e, data2[i])
            break
        elif e+1 == len(data1) :
            data1.append(data2[i])

if data1 == [] :
    data1 = data2

for i in data1 :
    print(i)