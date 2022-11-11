def is_odd(n):
    if n%2 == 1 :
        return True
    return False
def has_odds(x):
    for i in x :
        if i%2 == 1 :
            return True
    return False
def all_odds(x):
    for i in x :
        if i%2 == 0 :
            return False
    return True
def no_odds(x):
    for i in x :
        if i%2 == 1 :
            return False
    return True
def get_odds(x):
    y = []
    for i in x :
        if i%2 == 1 :
            y += [i]
    return y
def zip_odds(a, b):
    x = get_odds(a)
    y = get_odds(b)
    z = []
    while x != [] or y != [] :
        if x != [] :
            z += [x[0]]
            x.pop(0)
        if y != [] :
            z += [y[0]]
            y.pop(0)
    return z
exec(input().strip())