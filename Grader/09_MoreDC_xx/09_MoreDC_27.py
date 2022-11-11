def knows(R,x,y):
    if y in R[x] :
        return True
    return False
def is_celeb(R,x):
    if R[x] != set() and R[x] != set(x) :
        return False
    for i in R :
        if x not in R[i] and x != i :
            return False
    return True
def find_celeb(R):
    for i in R :
        if is_celeb(R,i) :
            return i
    return None
def read_relations() :
    R = dict()
    while True :
        d = input().split()
        if len(d) == 1 :
            break
        for i in d :
            if i not in R :
                R[i] = set()
        R[d[0]].add(d[1])
    return R
def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip())