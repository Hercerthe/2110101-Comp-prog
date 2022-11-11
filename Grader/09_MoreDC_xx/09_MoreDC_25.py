def row_number(t, e):
    for i in range(len(t)) :
        if e in t[i] :
            return i
def flatten(t):
    x = []
    for i in t :
        for e in i :
            x += [e]
    x.remove(0)
    return x
def inversions(x):
    count = 0
    y = x[0]
    x.pop(0)
    while x != [] :
        for i in x :
            if y > i :
                count += 1
        y = x[0]
        x.pop(0)
    return count
def solvable(t):
    if len(t) % 2 == 1 :
        if inversions(flatten(t)) % 2 == 0 :
            return True
    if len(t) % 2 == 0 :
        if inversions(flatten(t)) % 2 == 1 :
            if row_number(t, 0) % 2 == 0 :
                return True
        if inversions(flatten(t)) % 2 == 0 :
            if row_number(t, 0) % 2 == 1 :
                return True
    return False
exec(input().strip())