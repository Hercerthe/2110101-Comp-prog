def convex_polygon_area(p):
    x = []
    y = []
    pos = 0
    neg = 0
    for i in p :
        x.append(i[0])
        y.append(i[1])
    x.append(x[0])
    y.append(y[0])
    for i in range(len(x)-1) :
        pos += x[i]*y[i+1]
        neg += x[i+1]*y[i]
    return ((0.5*(pos-neg))**2)**0.5
    
def is_heterogram(s):
    x = []
    for i in s :
        i = i.lower()
        if not i.isalpha() :
            continue
        elif i not in x :
            x.append(i)
        elif i in x :
            return False
    return True

def replace_ignorecase(s, a, b):
    news = []
    while s != "" :
        if s[0:len(a)].lower() == a.lower() :
            news.append(b)
            s = s[len(a):]
        elif len(s) <= len(a) :
            news.append(s)
            s = ""
        else :
            news.append(s[0])
            s = s[1:]
    return "".join(news)

def top3(votes):
    top = []
    for i in votes :
        top.append([int("-"+str(votes[i])), i])
    top = sorted(top)
    top = top[0:3]
    for i in range(len(top)) :
        top[i] = top[i][1]
    return top

for k in range(2):
    exec(input().strip())