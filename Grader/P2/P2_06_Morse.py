x = 0
data = []
for i in open(input(), "r") :
    if x == 0 :
        pattern = i.replace("\n", "")
        x += 1
    elif x == 1 :
        text = i.replace("\n", "")
        x += 1
    elif x == 2 :
        data.append(i.replace("\n", ""))
morse = {}
morse2 = {}
text = text[1:-1].split("[")
for i in text :
    i = i.split("]")
    morse[i[0]] = i[1]
    morse2[i[1]] = i[0]
if pattern not in ["T2M", "M2T"] :
    print("Invalid code")
elif pattern == "T2M" :
    for i in data :
        x = []
        for e in i :
            if e not in morse :
                print("Invalid : {}".format(i))
                x = []
                break
            else :
                x.append(morse[e])
        if x != [] :
            print(" ".join(x))
elif pattern == "M2T" :
    for i in data :
        i = i.strip().split()
        x = []
        for e in i :
            if e not in morse2 :
                print("Invalid :", " ".join(i))
                x = []
                break
            x.append(morse2[e])
        if x != [] :
            print("".join(x))