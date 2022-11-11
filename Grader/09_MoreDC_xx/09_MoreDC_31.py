def gcd(a,b):
    while b != 0:
        a,b = b, a%b
    return a

def is_coprime(a, b , c) :
    y = [-1, 1]
    x = gcd(gcd(a, b), gcd(b, c))
    if x not in y :
            return False
    return True

def primitive_Pythagorean_triples(max_len) :
    triple = []
    for i in range(3,max_len-1) :
        for j in range(i+1,max_len) :
            k = (((i**2)+(j**2))**0.5)
            if (k%1 == 0) and  is_coprime(i, j, k) and (k <= max_len) :
                triple.append([int(k), i, j])
    triple = sorted(triple)
    for i in range(len(triple)) :
        triple[i][0],triple[i][1],triple[i][2] = triple[i][1],triple[i][2],triple[i][0]
    return triple

exec(input().strip())