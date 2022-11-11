def convolute(M, K):
    x = 0
    for i in range(len(M)) :
        for e in range(len(M[0])) :
            x += M[i][e]*K[i][e]
    return x
exec(input().strip())