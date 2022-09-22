def make_int_list(x):
    if len(x) == 0 :
        return []
    x = x.split(" ")
    for e in range(len(x)) :
        x[e] = int(x[e])
    return x

def is_odd(e):
    if e%2 == 1 :
        return True
    elif e%2 == 0 :
        return False

def odd_list(alist):
    list = []
    for i in alist :
        if is_odd(i) is True :
            list += [i]
    return list 
def sum_square(alist):
    sigma = 0
    for i in alist :
        sigma += i**2
    return sigma

exec(input().strip())