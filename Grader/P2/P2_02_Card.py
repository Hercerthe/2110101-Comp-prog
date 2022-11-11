card = {"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"T":10,"J":11,"Q":12,"K":13,"C":1,"D":2,"H":3,"S":4,}
x = input().replace("C","C ").replace("D","D ").replace("H","H ").replace("S","S ").strip().split(" ")
value = []
for i in range(len(x)-1) :
    if x[i][0] != x[i+1][0] :
        value += [card[x[i][0]] - card[x[i+1][0]]]
    else :
        value += [card[x[i][1]] - card[x[i+1][1]]]
for i in range(len(value)) :
    value[i] = str(value[i])
for i in range(len(value)) :
    if int(value[i]) > 0 :
        value[i] = "+" + value[i]
print("".join(value))