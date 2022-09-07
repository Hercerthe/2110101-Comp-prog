number = [int(e) for e in input().split(" ")]
result = []
for i in range(len(number)) :
    if number[i] not in result :
        result += [number[i]]
result = sorted(result)
print(len(result))
print(result[:10])