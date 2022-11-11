def read_matrix():
    m = []
    nrows = int(input())
    for k in range(nrows):
        x = input().split()
        r = []
        for e in x:
            r.append( float(e) )
        m.append(r)
    return m

def mult_c(c, A):
    for i in range(len(A)) :
        for e in range(len(A[i])) :
            A[i][e] *= c
    return A

def mult(A, B):
    C = []
    F = []
    for i in range(len(B[0])) :
        x = []
        for e in B :
            x += [e[i]]
        F += [x]
    for i in A :
        x = []
        for e in F :
            y = []
            for r in range(len(A[0])) :
                y += [i[r]*e[r]]
            x += [sum(y)]
        C += [x]
    return C
exec(input().strip())