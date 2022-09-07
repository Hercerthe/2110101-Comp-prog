x = list(input())

for e in range(0,len(x)) :
    if x[e] == "(" :
        x[e] = "["
    elif x[e] == ")" :
        x[e] = "]"
    elif x[e] == "[" :
        x[e] = "("
    elif x[e] == "]" :
        x[e] = ")"

print("".join(x))