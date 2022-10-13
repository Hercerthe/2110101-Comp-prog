data = input().split(" ")
score = []
for i in open(data[0], "r") :
    if data[1][-2:] not in i[:2] :
        continue
    score += [float(i[11:].replace("\n", ""))]
if score == [] :
    print("No data")
else :
    print(min(score), max(score), (sum(score)/len(score)))