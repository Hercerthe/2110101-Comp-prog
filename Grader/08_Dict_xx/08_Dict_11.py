def reverse(d):
    new_d = {}
    for i in d :
        new_d[d[i]] = i
    return new_d
def keys(d, v):
    listed = []
    for i in d :
        if d[i] == v :
            listed += [i]
    return listed
exec(input().strip())