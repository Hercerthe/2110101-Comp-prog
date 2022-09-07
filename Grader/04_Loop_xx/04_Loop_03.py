answer = list(input())
input_answer = list(input())
score = 0

if len(answer) == len(input_answer) :
    for x in range(0,len(answer)) :
        if answer[x] == input_answer[x] :
            score += 1
    print(score)

else :
    print("Incomplete answer")