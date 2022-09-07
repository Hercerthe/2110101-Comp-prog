def choose(stu1, stu2) :

    status1 = 1
    status2 = 1
    grade = ["A", "B", "C"]


    if stu1[2] == "A" and stu1[3] in grade and stu1[4] in grade :
        pass
    else :
        status1 = 0
    

    if stu2[2] == "A" and stu2[3] in grade and stu2[4] in grade :
        pass
    else :
        status2 = 0


    if status1 == 1 and status2 == 0 :
        return [stu1[0]]
    if status1 == 0 and status2 == 1 :
        return [stu2[0]]

    if stu1[1] > stu2[1] and status1 == status2 == 1 :
        return [stu1[0]]
        status1 = 0
    if stu1[1] < stu2[1] and status1 == status2 == 1 :
        return [stu2[0]]
        status1 = 0
    if stu1[1] == stu2[1] :
        pass

    if stu1[3] < stu2[3] and status1 == status2 == 1 :
        return [stu1[0]]
        status1 = 0
    if stu1[3] > stu2[3] and status1 == status2 == 1 :
        return [stu2[0]]
        status1 = 0
    if stu1[3] == stu2[3] :
        pass

    if stu1[4] < stu2[4] and status1 == status2 == 1 :
        return [stu1[0]]
        status1 = 0
    if stu1[4] > stu2[4] and status1 == status2 == 1 :
        return [stu2[0]]
        status1 = 0
    if stu1[4] == stu2[4] :
        pass

    if stu1[1:] == stu2[1:] :
        return [stu1[0] , stu2[0]]

    return []

exec(input()) # DON'T remove this line