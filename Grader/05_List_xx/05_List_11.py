digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
data = input()
result = []
for e in range(10) :
    if digit[e] not in data :
        result += [digit[e]]

if result == [] :
        result = ["None"]

print(",".join(result))