def to_Thai( N ):
    N = str(N)
    unit = {"0":"soon", "1":"neung", "2":"song", "3":"sam", "4":"si", "5":"ha", "6":"hok", "7":"chet", "8":"paet", "9":"kao"}
    read = []
    number = []
    for i in N :
        number.append(i)
    number.reverse()
    for i in range(len(number)) :
        number[i] = number[i]+("0"*i)
    number.reverse()
    if number == ["0"] :
        return "soon"
    for i in number :
        if i in "0000" :
            continue
        elif int(i) >= 1000 :
            read += [unit[i[0]], "pun"]
        elif 1000 > int(i) >= 100 :
            read += [unit[i[0]], "roi"]
        elif 100 > int(i) >= 10 :
            if unit[i[0]] == "song" :
                read += ["yi", "sip"]
            elif unit[i[0]] == "neung" :
                read += ["sip"]
            else :
                read += [unit[i[0]], "sip"]
        elif 10 > int(i) :
            if unit[i[0]] == "neung" and ("sip" in read or "roi" in read or "pun" in read) :
                read += ["et"]
            else :
                read += [unit[i[0]]]
    return " ".join(read)
exec(input().strip())