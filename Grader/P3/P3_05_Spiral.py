def spiral_square(n):
    x = 0
    sq = list()
    pos = [(n-1)//2, (n-1)//2]
    right = True
    up = True
    for i in range(n) :
        sq.append(list("-"*n))
    for i in range((n*2)-1) :
        if i == 0 :
            x += 1
            sq[pos[0]][pos[1]] = x
        elif i%2 == 1 :
            i = round((i/2)+0.1)
            if right :
                for j in range(i) :
                    pos[1] += 1
                    x += 1
                    sq[pos[0]][pos[1]] = x
                right = False
            else :
                for j in range(i) :
                    pos[1] -= 1
                    x += 1
                    sq[pos[0]][pos[1]] = x
                right = True
        elif i%2 == 0 :
            i = round((i/2)+0.1)
            if up :
                for j in range(i) :
                    pos[0] -= 1
                    x += 1
                    sq[pos[0]][pos[1]] = x
                up = False
            else :
                for j in range(i) :
                    pos[0] += 1
                    x += 1
                    sq[pos[0]][pos[1]] = x
                up = True
    for k in range(i) :
        pos[1] += 1
        x += 1
        sq[pos[0]][pos[1]] = x
    return sq
def print_square(S):
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip())