def index_of(grades, ID):
    for i in range(len(grades)) :
        if ID == grades[i][0] :
            return i
    return -1
def upgrade(grades, IDs):
    grade = ["A", "B+", "B", "C+", "C", "D+", "D", "F"]

    for i in range(len(grades)) :
        if grades[i][0] in IDs :
            for e in range(len(grade)) :
                if grades[i][1] == grade[0] :
                    break
                elif grades[i][1] == grade[e] :
                    grades[i][1] = grade[e - 1]

    grades = sorted(grades)
    global g
    g = grades


exec(input())
exec(input())
exec(input())