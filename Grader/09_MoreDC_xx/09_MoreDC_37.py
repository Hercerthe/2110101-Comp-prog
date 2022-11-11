capable = dict()
student = list()
data = list()
for i in range(int(input())) :
    x = input().split()
    capable[x[0]] = int(x[1])
for i in range(int(input())) :
    x = input().split()
    student.append([float(x[1]), x[0], x[2:]])
student = sorted(student, reverse=True)
for i in student :
    for e in i[2] :
        if capable[e] > 0 :
            capable[e] -= 1
            data.append([i[1], e])
            break
data = sorted(data)
for i in data :
    print(" ".join(i))