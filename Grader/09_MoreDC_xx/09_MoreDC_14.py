course = {}
teacher = {}
for i in open(input(), "r") :
    i = i.replace("\n", "").split(",")
    course[i[0]] = i[1]
for i in open(input(), "r") :
    i = i.replace("\n", "").split(",")
    teacher[i[0]] = i[1]
for i in open(input(), "r") :
    i = i.replace("\n", "").split(",")
    if i[0] not in course or i[1] not in teacher :
        print("record error")
    else :
        print("{},{}".format(course[i[0]], teacher[i[1]]))