def grade_mcq(sol, ans) :
    score = 0
    if len(sol) == len(ans) :
        for x in range(0,len(sol)) :
            if sol[x] == ans[x] :
                score += 1
        return score
    else :
        return -1

exec(input())