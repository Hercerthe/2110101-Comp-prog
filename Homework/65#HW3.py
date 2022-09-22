# HW3_List_processing_Function (ไม่ลบหรือแก้ไขบรรทัดนี้ หรือเพิ่มอะไรก่อนบรรทัดนี้ โดยเด็ดขาด)

def get_weighted_score(weights, grades):
    
    score = 0
    grades = list(grades)
    for i in range(len(grades)) :
        grades[i] = ["F", "D", "C", "B", "A"].index(grades[i])
    
    for i in range(len(grades)) :
        score += grades[i] * weights[i]

    return score

def student_sorting(stu_weight_scores, n):

    stu_list = []
    for i in range(1, len(stu_weight_scores), 2) :
            stu_list += [[stu_weight_scores[i], stu_weight_scores[i-1]]]
    stu_list = sorted(stu_list, reverse = True)
    result = []
    for i in range(len(stu_list)) :
        if n == 0 :
            break
        elif result == [] and n > 0 :
            result += [stu_list[i][1]]
            n -= 1
        elif stu_list[i-1][0] == stu_list[i][0] and n >= 0 :
            result += [stu_list[i][1]]
        elif stu_list[i-1][0] != stu_list[i][0] and n > 0 :
            result += [stu_list[i][1]]
            n -= 1
    return sorted(result)

def test():

    my_weighted_score = get_weighted_score([1], 'D')	
    print(my_weighted_score)

    S = []
    n = 4
    selected_students = student_sorting(S, n)
    print(selected_students)

test()