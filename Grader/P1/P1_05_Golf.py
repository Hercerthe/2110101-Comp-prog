data = []
sum_par = 0
sum_stroke = 0
sum_fixed_stroke = 0
for i in range(9) :
    hole = i + 1
    raw = [int(e) for e in input().split(" ")]
    fixed_stroke = min((raw[0] + 2), raw[1])
    if raw[2] == 1 :
        data += [[hole, raw[0], raw[1], raw[2], fixed_stroke]]
    elif raw[2] == 0 :
        data += [[hole, raw[0], raw[1], raw[2], 0]]

for i in range (9) :
    sum_par += data[i][1]
    sum_stroke += data[i][2]
    sum_fixed_stroke += data[i][4]

handicap = (0.8*(1.5*sum_fixed_stroke - sum_par))
handicap //= 1
point = sum_stroke - handicap

print(int(sum_stroke))
print(int(handicap))
print(int(point))