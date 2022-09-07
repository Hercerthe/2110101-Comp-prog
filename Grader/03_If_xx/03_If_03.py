score = [float(x) for x in input().split()]
score = sorted(score)
score = (sum(score[1:-1])) / len(score[1:-1])
print(round(score, 2))