data_set1 = input().split(" ")
data_set2 = input().split(" ")
status1 = 1
status2 = 1
grade = ["A", "B", "C"]


if data_set1[2] == "A" and data_set1[3] in grade and data_set1[4] in grade :
    pass
else :
    status1 = 0
    

if data_set2[2] == "A" and data_set2[3] in grade and data_set2[4] in grade :
    pass
else :
    status2 = 0


if status1 == 1 and status2 == 0 :
    print(data_set1[0])
if status1 == 0 and status2 == 1 :
    print(data_set2[0])
if status1 == 0 and status2 == 0 :
    print("None")

if data_set1[1] > data_set2[1] and status1 == status2 == 1 :
    print(data_set1[0])
    status1 = 0
if data_set1[1] < data_set2[1] and status1 == status2 == 1 :
    print(data_set2[0])
    status1 = 0
if data_set1[1] == data_set2[1] :
    pass

if data_set1[3] < data_set2[3] and status1 == status2 == 1 :
    print(data_set1[0])
    status1 = 0
if data_set1[3] > data_set2[3] and status1 == status2 == 1 :
    print(data_set2[0])
    status1 = 0
if data_set1[3] == data_set2[3] :
    pass

if data_set1[4] < data_set2[4] and status1 == status2 == 1 :
    print(data_set1[0])
    status1 = 0
if data_set1[4] > data_set2[4] and status1 == status2 == 1 :
    print(data_set2[0])
    status1 = 0
if data_set1[4] == data_set2[4] :
    pass

if data_set1[1:] == data_set2[1:] :
    print("Both")