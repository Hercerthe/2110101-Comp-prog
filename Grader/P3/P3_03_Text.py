data = open(input(), "r").read().replace("\n", ".")
newdata = list()
k = int(input())
ruler = str()
for i in range(k//10) :
    ruler += '-'*9 + str(i+1)
if k%10 != 0 :
    ruler += '-'*(k%10)
print(ruler)
while len(data) > 0 :
    line = str()
    while data[0] == "." :
        data = data[1:]
    if len(data) > k :
        for i in range(k-1,-1,-1) :
            if (data[i+1] == "." and data[i] != ".") or data[i] == "." :
                line = data[0:i+1]
                data = data[i+1:]
                break
    elif len(data) <= k :
        line = data
        data = str()
    if "." not in line and data.find(".") > 0 :
        line += data[:data.find(".")]
        data = data[data.find("."):]
    elif "." not in line and "." not in data :
        line += data
        data = str()
    newdata.append(line)
for i in newdata :
    print(i.strip("."))