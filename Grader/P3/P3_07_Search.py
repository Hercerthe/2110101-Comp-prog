data = dict()
search = str()
for i in range(int(input())) :
    fname = input().strip()
    context = input().strip().lower().split()
    data[fname] = context
while search != "-1" :
    search = input().strip().lower()
    if search == "-1" :
        break
    score = list()
    for i in data :
        allword = 0
        word = set()
        searchword = 0
        for e in data[i] :
            if e == "" :
                continue
            if e == search :
                searchword += 1
            word.add(e)
            allword += 1
        score.append([(searchword/allword)*(1/len(word)), i])
    score = sorted(score, reverse=True)
    if score[0][0] > 0 :
        print(score[0][1])
    else :
        print("NOT FOUND")